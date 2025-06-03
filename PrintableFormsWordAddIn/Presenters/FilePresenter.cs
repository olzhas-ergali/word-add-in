using PrintableFormsWordAddIn.Application.Contracts.Services;
using PrintableFormsWordAddIn.Application.Contracts.Views;
using PrintableFormsWordAddIn.Application.Services;
using PrintableFormsWordAddIn.Application.Utils;
using System;
using System.IO;
using System.Threading.Tasks;

namespace PrintableFormsWordAddIn.Presenters
{
    public class FilePresenter
    {
        private readonly IFileView fileView;
        private readonly IPfApiService fileService;

        public FilePresenter(IFileView fileView) 
        {
            this.fileView = fileView;
            this.fileView.Selected += OnSelected;
            this.fileService = new PfApiService(Globals.ThisAddIn.MemoryCacheService);
            AsyncHelper.RunSync(() => RefreshFileViewData());
        }

        private async Task RefreshFileViewData()
        {
            var filesList = await fileService.GetTemplateFiles();

            fileView.RefreshFileList(filesList);
        }

        private async Task OnSelected(object sender, EventArgs e) 
        {
            fileView.ShowSuccess();

            var selectedFileStream = await fileService.GetPfDocument(Globals.ThisAddIn.SelectedDocument.DocumentId);
            
            string tempFilePath = Path.Combine(Path.GetTempPath(), Globals.ThisAddIn.SelectedDocument.FileName);
            using (FileStream outputFileStream = new FileStream(tempFilePath, FileMode.Create, FileAccess.Write))
            {
                selectedFileStream.CopyTo(outputFileStream);
            }

            Microsoft.Office.Interop.Word.Document activeDocument = Globals.ThisAddIn.Application.ActiveDocument;
            //Check, if Active Window is blank, then we can close it. Once the new Window is Opened. If not, 
            //we'll open the document in new window
            bool closeParentWindow = activeDocument.Content.End - activeDocument.Content.Start == 1;
            string activeDocName = activeDocument.Name;

            //Add the new document which's supposed to open
            Microsoft.Office.Interop.Word.Document newDoc = Globals.ThisAddIn.Application.Documents.Open(tempFilePath);
            newDoc.ActiveWindow.Caption = Globals.ThisAddIn.SelectedDocument.FileName;

            if (closeParentWindow)
            {
                //If Earlier Window/ Document Could be closed. Then need to invoke Close
                Microsoft.Office.Interop.Word.Document docToClose = Globals.ThisAddIn.Application.Documents[activeDocName];
                docToClose.Close(Microsoft.Office.Interop.Word.WdSaveOptions.wdDoNotSaveChanges);
            }
        }
    }
}
