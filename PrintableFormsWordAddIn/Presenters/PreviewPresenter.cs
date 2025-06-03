using PrintableFormsWordAddIn.Application.Services;
using PrintableFormsWordAddIn.Application.Utils;
using System;
using System.Collections.Generic;
using System.Linq;

namespace PrintableFormsWordAddIn.Presenters
{
    public class PreviewPresenter
    {
        private readonly PfApiService apiService;
        
        public PreviewPresenter() 
        {
            apiService = new PfApiService(Globals.ThisAddIn.MemoryCacheService);
        }

        public void ReplaceFields()
        {
            var wordApp = Globals.ThisAddIn.Application;
            var document = wordApp.ActiveDocument;

            var variables = document.Variables;
            var idsToSend = new List<string>();
            for(int i = 1; i <= variables.Count; i++)
            {
                idsToSend.Add(variables[i].Name);
            }

            var values = AsyncHelper.RunSync(() => apiService.GetDocumentVariablesWithValues(idsToSend));

            for (int i = 1; i <= variables.Count; i++)
            {
                var guid = Guid.Parse(variables[i].Name.Replace('_', '-'));

                var value = values.FirstOrDefault(x => x.Id == guid)?.Value ?? "Пустое поле";

                variables[i].Value = value;
            }

            document.Fields.Update();
        }
    }
}
