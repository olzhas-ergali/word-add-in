namespace PrintableFormsWordAddIn.Views
{
    partial class FileView
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.bindingSource1 = new System.Windows.Forms.BindingSource(this.components);
            this.bindingSource2 = new System.Windows.Forms.BindingSource(this.components);
            this.bindingSource3 = new System.Windows.Forms.BindingSource(this.components);
            this.FileDataGridView = new System.Windows.Forms.DataGridView();
            this.SearchFileLabel = new System.Windows.Forms.Label();
            this.SearchFileTextBox = new System.Windows.Forms.TextBox();
            this.pfDocumentBindingSource1 = new System.Windows.Forms.BindingSource(this.components);
            this.keyCloakTokenBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.keyCloakTokenBindingSource1 = new System.Windows.Forms.BindingSource(this.components);
            this.keyCloakTokenBindingSource2 = new System.Windows.Forms.BindingSource(this.components);
            this.pfDocumentBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.pfDocumentBindingSource2 = new System.Windows.Forms.BindingSource(this.components);
            this.fileNameDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.OrganizationName = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.createdAtDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource3)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.FileDataGridView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pfDocumentBindingSource1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.keyCloakTokenBindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.keyCloakTokenBindingSource1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.keyCloakTokenBindingSource2)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pfDocumentBindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pfDocumentBindingSource2)).BeginInit();
            this.SuspendLayout();
            // 
            // FileDataGridView
            // 
            this.FileDataGridView.AllowUserToAddRows = false;
            this.FileDataGridView.AllowUserToDeleteRows = false;
            this.FileDataGridView.AutoGenerateColumns = false;
            this.FileDataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.FileDataGridView.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.fileNameDataGridViewTextBoxColumn,
            this.OrganizationName,
            this.createdAtDataGridViewTextBoxColumn});
            this.FileDataGridView.DataSource = this.pfDocumentBindingSource1;
            this.FileDataGridView.Location = new System.Drawing.Point(12, 51);
            this.FileDataGridView.MultiSelect = false;
            this.FileDataGridView.Name = "FileDataGridView";
            this.FileDataGridView.ReadOnly = true;
            this.FileDataGridView.RowHeadersWidthSizeMode = System.Windows.Forms.DataGridViewRowHeadersWidthSizeMode.AutoSizeToDisplayedHeaders;
            this.FileDataGridView.RowTemplate.ReadOnly = true;
            this.FileDataGridView.RowTemplate.Resizable = System.Windows.Forms.DataGridViewTriState.True;
            this.FileDataGridView.SelectionMode = System.Windows.Forms.DataGridViewSelectionMode.CellSelect;
            this.FileDataGridView.Size = new System.Drawing.Size(364, 387);
            this.FileDataGridView.TabIndex = 0;
            this.FileDataGridView.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.FileDataGridView_CellContentClick);
            // 
            // SearchFileLabel
            // 
            this.SearchFileLabel.AutoSize = true;
            this.SearchFileLabel.Location = new System.Drawing.Point(12, 9);
            this.SearchFileLabel.Name = "SearchFileLabel";
            this.SearchFileLabel.Size = new System.Drawing.Size(39, 13);
            this.SearchFileLabel.TabIndex = 1;
            this.SearchFileLabel.Text = "Поиск";
            // 
            // SearchFileTextBox
            // 
            this.SearchFileTextBox.Location = new System.Drawing.Point(12, 25);
            this.SearchFileTextBox.Name = "SearchFileTextBox";
            this.SearchFileTextBox.Size = new System.Drawing.Size(364, 20);
            this.SearchFileTextBox.TabIndex = 2;
            this.SearchFileTextBox.TextChanged += new System.EventHandler(this.SearchFileTextBox_TextChanged);
            // 
            // pfDocumentBindingSource1
            // 
            this.pfDocumentBindingSource1.DataSource = typeof(PrintableFormsWordAddIn.Application.Models.PfDocument);
            // 
            // keyCloakTokenBindingSource
            // 
            this.keyCloakTokenBindingSource.DataSource = typeof(PrintableFormsWordAddIn.Application.Models.KeyCloakToken);
            // 
            // keyCloakTokenBindingSource1
            // 
            this.keyCloakTokenBindingSource1.DataSource = typeof(PrintableFormsWordAddIn.Application.Models.KeyCloakToken);
            // 
            // keyCloakTokenBindingSource2
            // 
            this.keyCloakTokenBindingSource2.DataSource = typeof(PrintableFormsWordAddIn.Application.Models.KeyCloakToken);
            // 
            // pfDocumentBindingSource
            // 
            this.pfDocumentBindingSource.DataSource = typeof(PrintableFormsWordAddIn.Application.Models.PfDocument);
            // 
            // pfDocumentBindingSource2
            // 
            this.pfDocumentBindingSource2.DataSource = typeof(PrintableFormsWordAddIn.Application.Models.PfDocument);
            // 
            // fileNameDataGridViewTextBoxColumn
            // 
            this.fileNameDataGridViewTextBoxColumn.DataPropertyName = "FileName";
            this.fileNameDataGridViewTextBoxColumn.HeaderText = "FileName";
            this.fileNameDataGridViewTextBoxColumn.Name = "fileNameDataGridViewTextBoxColumn";
            this.fileNameDataGridViewTextBoxColumn.ReadOnly = true;
            // 
            // OrganizationName
            // 
            this.OrganizationName.DataPropertyName = "OrganizationName";
            this.OrganizationName.HeaderText = "OrganizationName";
            this.OrganizationName.Name = "OrganizationName";
            this.OrganizationName.ReadOnly = true;
            // 
            // createdAtDataGridViewTextBoxColumn
            // 
            this.createdAtDataGridViewTextBoxColumn.DataPropertyName = "CreatedAt";
            this.createdAtDataGridViewTextBoxColumn.HeaderText = "CreatedAt";
            this.createdAtDataGridViewTextBoxColumn.Name = "createdAtDataGridViewTextBoxColumn";
            this.createdAtDataGridViewTextBoxColumn.ReadOnly = true;
            // 
            // FileView
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSize = true;
            this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.ClientSize = new System.Drawing.Size(390, 450);
            this.Controls.Add(this.SearchFileTextBox);
            this.Controls.Add(this.SearchFileLabel);
            this.Controls.Add(this.FileDataGridView);
            this.Name = "FileView";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Select File";
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.bindingSource3)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.FileDataGridView)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pfDocumentBindingSource1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.keyCloakTokenBindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.keyCloakTokenBindingSource1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.keyCloakTokenBindingSource2)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pfDocumentBindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pfDocumentBindingSource2)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.BindingSource keyCloakTokenBindingSource;
        private System.Windows.Forms.BindingSource keyCloakTokenBindingSource1;
        private System.Windows.Forms.BindingSource keyCloakTokenBindingSource2;
        private System.Windows.Forms.BindingSource bindingSource1;
        private System.Windows.Forms.BindingSource bindingSource2;
        private System.Windows.Forms.BindingSource bindingSource3;
        private System.Windows.Forms.BindingSource pfDocumentBindingSource;
        private System.Windows.Forms.DataGridView FileDataGridView;
        private System.Windows.Forms.BindingSource pfDocumentBindingSource1;
        private System.Windows.Forms.Label SearchFileLabel;
        private System.Windows.Forms.TextBox SearchFileTextBox;
        private System.Windows.Forms.BindingSource pfDocumentBindingSource2;
        private System.Windows.Forms.DataGridViewTextBoxColumn fileNameDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn OrganizationName;
        private System.Windows.Forms.DataGridViewTextBoxColumn createdAtDataGridViewTextBoxColumn;
    }
}