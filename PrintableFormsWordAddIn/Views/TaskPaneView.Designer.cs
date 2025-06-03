namespace PrintableFormsWordAddIn.Views
{
    partial class TaskPaneView
    {
        /// <summary> 
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary> 
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором компонентов

        /// <summary> 
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.VariableCheckedListBox = new System.Windows.Forms.CheckedListBox();
            this.SuspendLayout();
            // 
            // VariableCheckedListBox
            // 
            this.VariableCheckedListBox.FormattingEnabled = true;
            this.VariableCheckedListBox.Location = new System.Drawing.Point(16, 15);
            this.VariableCheckedListBox.Name = "VariableCheckedListBox";
            this.VariableCheckedListBox.Size = new System.Drawing.Size(248, 634);
            this.VariableCheckedListBox.TabIndex = 0;
            // 
            // TaskPaneView
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.VariableCheckedListBox);
            this.Name = "TaskPaneView";
            this.Size = new System.Drawing.Size(278, 667);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.CheckedListBox VariableCheckedListBox;
    }
}
