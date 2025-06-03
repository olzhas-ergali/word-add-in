namespace PrintableFormsWordAddIn
{
    partial class RibbonUI : Microsoft.Office.Tools.Ribbon.RibbonBase
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        public RibbonUI()
            : base(Globals.Factory.GetRibbonFactory())
        {
            InitializeComponent();
        }

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
            this.MainTab = this.Factory.CreateRibbonTab();
            this.MainGroup = this.Factory.CreateRibbonGroup();
            this.LoginButton = this.Factory.CreateRibbonButton();
            this.LogoutButton = this.Factory.CreateRibbonButton();
            this.SelectReportButton = this.Factory.CreateRibbonButton();
            this.PreviewButton = this.Factory.CreateRibbonButton();
            this.MainTab.SuspendLayout();
            this.MainGroup.SuspendLayout();
            this.SuspendLayout();
            // 
            // MainTab
            // 
            this.MainTab.ControlId.ControlIdType = Microsoft.Office.Tools.Ribbon.RibbonControlIdType.Office;
            this.MainTab.Groups.Add(this.MainGroup);
            this.MainTab.Label = "Печатные формы";
            this.MainTab.Name = "MainTab";
            // 
            // MainGroup
            // 
            this.MainGroup.Items.Add(this.LoginButton);
            this.MainGroup.Items.Add(this.LogoutButton);
            this.MainGroup.Items.Add(this.SelectReportButton);
            this.MainGroup.Items.Add(this.PreviewButton);
            this.MainGroup.Label = "Управление данными";
            this.MainGroup.Name = "MainGroup";
            // 
            // LoginButton
            // 
            this.LoginButton.ControlSize = Microsoft.Office.Core.RibbonControlSize.RibbonControlSizeLarge;
            this.LoginButton.Image = global::PrintableFormsWordAddIn.Properties.Resources.login;
            this.LoginButton.Label = "Войти";
            this.LoginButton.Name = "LoginButton";
            this.LoginButton.ShowImage = true;
            this.LoginButton.Click += new Microsoft.Office.Tools.Ribbon.RibbonControlEventHandler(this.LoginButton_Click);
            // 
            // LogoutButton
            // 
            this.LogoutButton.ControlSize = Microsoft.Office.Core.RibbonControlSize.RibbonControlSizeLarge;
            this.LogoutButton.Image = global::PrintableFormsWordAddIn.Properties.Resources.Exit;
            this.LogoutButton.Label = "Выйти";
            this.LogoutButton.Name = "LogoutButton";
            this.LogoutButton.ShowImage = true;
            this.LogoutButton.Click += new Microsoft.Office.Tools.Ribbon.RibbonControlEventHandler(this.LogoutButton_Click);
            // 
            // SelectReportButton
            // 
            this.SelectReportButton.ControlSize = Microsoft.Office.Core.RibbonControlSize.RibbonControlSizeLarge;
            this.SelectReportButton.Image = global::PrintableFormsWordAddIn.Properties.Resources.Select_report;
            this.SelectReportButton.Label = "Выбрать документ";
            this.SelectReportButton.Name = "SelectReportButton";
            this.SelectReportButton.ShowImage = true;
            this.SelectReportButton.Click += new Microsoft.Office.Tools.Ribbon.RibbonControlEventHandler(this.SelectReportButton_Click);
            // 
            // PreviewButton
            // 
            this.PreviewButton.ControlSize = Microsoft.Office.Core.RibbonControlSize.RibbonControlSizeLarge;
            this.PreviewButton.Image = global::PrintableFormsWordAddIn.Properties.Resources.Report_Data;
            this.PreviewButton.Label = "Предпосмотр";
            this.PreviewButton.Name = "PreviewButton";
            this.PreviewButton.ShowImage = true;
            this.PreviewButton.Click += new Microsoft.Office.Tools.Ribbon.RibbonControlEventHandler(this.PreviewButton_Click);
            // 
            // RibbonUI
            // 
            this.Name = "RibbonUI";
            this.RibbonType = "Microsoft.Word.Document";
            this.Tabs.Add(this.MainTab);
            this.Load += new Microsoft.Office.Tools.Ribbon.RibbonUIEventHandler(this.RibbonUI_Load);
            this.MainTab.ResumeLayout(false);
            this.MainTab.PerformLayout();
            this.MainGroup.ResumeLayout(false);
            this.MainGroup.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        internal Microsoft.Office.Tools.Ribbon.RibbonTab MainTab;
        internal Microsoft.Office.Tools.Ribbon.RibbonGroup MainGroup;
        internal Microsoft.Office.Tools.Ribbon.RibbonButton LoginButton;
        internal Microsoft.Office.Tools.Ribbon.RibbonButton LogoutButton;
        internal Microsoft.Office.Tools.Ribbon.RibbonButton SelectReportButton;
        internal Microsoft.Office.Tools.Ribbon.RibbonButton PreviewButton;
    }

    partial class ThisRibbonCollection
    {
        internal RibbonUI RibbonUI
        {
            get { return this.GetRibbon<RibbonUI>(); }
        }
    }
}
