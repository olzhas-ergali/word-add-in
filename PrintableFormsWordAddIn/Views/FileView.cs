using PrintableFormsWordAddIn.Application.Contracts.Views;
using PrintableFormsWordAddIn.Application.Models;
using PrintableFormsWordAddIn.Application.Utils;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace PrintableFormsWordAddIn.Views
{
    public partial class FileView : Form, IFileView
    {
        private readonly List<PfDocument> fileList;

        public FileView()
        {
            InitializeComponent();
            this.fileList = new List<PfDocument>();
        }

        public void RefreshFileList(IEnumerable<PfDocument> list) 
        {
            fileList.AddRange(list);
            pfDocumentBindingSource1.DataSource = fileList;
            FileDataGridView.Refresh();
        }

        public event AsyncEventHandler Selected;

        public void ShowError(string message)
        {
            this.DialogResult = DialogResult.Abort;
            this.Close();
        }

        public void ShowSuccess()
        {
            this.DialogResult = DialogResult.OK;
            this.Close();
        }

        private void FileDataGridView_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            Globals.ThisAddIn.SelectedDocument = fileList[e.RowIndex];
            Selected.Invoke(sender, e);
        }

        private void SearchFileTextBox_TextChanged(object sender, EventArgs e)
        {
            var filteredList = fileList.Where(x => x.FileName.IndexOf(SearchFileTextBox.Text, StringComparison.InvariantCultureIgnoreCase) >= 0);
            pfDocumentBindingSource1.DataSource = filteredList;
            FileDataGridView.Refresh();
        }
    }
}
