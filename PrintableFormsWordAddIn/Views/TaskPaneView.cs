using Microsoft.Office.Interop.Word;
using PrintableFormsWordAddIn.Application.Contracts.Services;
using PrintableFormsWordAddIn.Application.Models;
using PrintableFormsWordAddIn.Application.Services;
using PrintableFormsWordAddIn.Application.Utils;
using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace PrintableFormsWordAddIn.Views
{
    public partial class TaskPaneView : UserControl
    {
        private Microsoft.Office.Interop.Word.Application wordApp;
        
        private readonly List<DocumentVariable> checklist;
        private readonly IPfApiService apiService;

        public TaskPaneView(Microsoft.Office.Interop.Word.Application wordApp, IMemoryCacheService memoryCacheService)
        {
            InitializeComponent();
            this.wordApp = wordApp;
            checklist = new List<DocumentVariable>
            {
                new DocumentVariable
                {
                    Id = Guid.Empty,
                    Name = "Факсимиле"
                }
            };
            apiService = new PfApiService(memoryCacheService);
            wordApp.DocumentOpen += RefreshVariables;
        }

        private void RefreshVariables(Document document)
        {
            var pfVariables = AsyncHelper.RunSync(() => apiService.GetDocumentVariables(Globals.ThisAddIn.SelectedDocument.DocumentId));

            checklist.AddRange(pfVariables);

            this.Controls.Clear();
            for (int i = 0; i < checklist.Count; i++)
            {
                var label = new Label()
                {
                    Name = checklist[i].Id.ToString().Replace('-', '_'),
                    Text = checklist[i].Name,
                    BorderStyle = BorderStyle.FixedSingle,
                    Padding = new Padding(5),
                    Margin = new Padding(3),
                    Cursor = Cursors.Hand,
                    AutoSize = true,
                    Location = new System.Drawing.Point(0, 32 * i),
                };
                label.MouseDown += Label_MouseDown; // Enable dragging
                
                this.Controls.Add(label);
            }

            this.Refresh();
        }

        private void Label_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                var label = (Label)sender;
                var text = label.Text;
                var id = label.Name;
                var result = label.DoDragDrop(text, DragDropEffects.Copy);

                if (result == DragDropEffects.Copy)
                {
                    var doc = wordApp.ActiveDocument;

                    try
                    {
                        doc.Variables.Add(id, text);
                    }
                    catch(Exception ex)
                    {
                        MessageBox.Show(ex.Message);
                    }

                    doc.Fields.Add(doc.Application.Selection.Range, WdFieldType.wdFieldDocVariable, id, true);
                    doc.Fields.Update();
                }
            }
        }
    }
}
