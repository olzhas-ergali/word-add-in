using Microsoft.Office.Interop.Word;
using PrintableFormsWordAddIn.Application.Contracts.Services;
using PrintableFormsWordAddIn.Application.Models;
using PrintableFormsWordAddIn.Application.Services;
using PrintableFormsWordAddIn.Views;
using System;

namespace PrintableFormsWordAddIn
{
    public partial class ThisAddIn
    {
        private TaskPaneView taskPane;
        private Microsoft.Office.Tools.CustomTaskPane pane;

        public IMemoryCacheService MemoryCacheService { get; private set; }
        public PfDocument SelectedDocument { get; set; }

        public EventHandler RefreshTaskPane;

        private void ThisAddIn_Startup(object sender, System.EventArgs e)
        {
            this.MemoryCacheService = new MemoryCacheService();
            taskPane = new TaskPaneView(this.Application, MemoryCacheService);
            Application.DocumentOpen += OnDocumentOpen;
        }

        private void ThisAddIn_Shutdown(object sender, System.EventArgs e)
        {
        }

        private void OnDocumentOpen(Document doc)
        {
            pane = this.CustomTaskPanes.Add(taskPane, "Data Checklist");
            pane.Visible = true;
        }

        #region Код, автоматически созданный VSTO

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InternalStartup()
        {
            this.Startup += new System.EventHandler(ThisAddIn_Startup);
            this.Shutdown += new System.EventHandler(ThisAddIn_Shutdown);
        }
        
        #endregion
    }
}
