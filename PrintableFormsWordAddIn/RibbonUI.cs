using Microsoft.Office.Tools.Ribbon;
using PrintableFormsWordAddIn.Presenters;
using PrintableFormsWordAddIn.Views;
using System.Windows.Forms;

namespace PrintableFormsWordAddIn
{
    public partial class RibbonUI
    {
        private void RibbonUI_Load(object sender, RibbonUIEventArgs e)
        {
            LoginButton.Visible = true;
            LogoutButton.Visible = false;
            SelectReportButton.Visible = false;
            PreviewButton.Visible = false;
            PreviewButton.Enabled = false;
        }

        private void LoginButton_Click(object sender, RibbonControlEventArgs e)
        {
            //var loginView = new LoginView();
            //var loginPresenter = new LoginPresenter(loginView);
            //if (loginView.ShowDialog() == DialogResult.OK)
            //{
                LoginButton.Visible = false;
                LogoutButton.Visible = true;
                SelectReportButton.Visible = true;
                PreviewButton.Visible = true;
            //}
        }

        private void LogoutButton_Click(object sender, RibbonControlEventArgs e)
        {
            LoginButton.Visible = true;
            LogoutButton.Visible = false;
            SelectReportButton.Visible = false;
            PreviewButton.Visible = false;
            PreviewButton.Enabled = false;
        }

        private void SelectReportButton_Click(object sender, RibbonControlEventArgs e)
        {
            var fileView = new FileView();
            var filePresenter = new FilePresenter(fileView);
            if(fileView.ShowDialog() == DialogResult.OK)
            {
                PreviewButton.Enabled = true;
            };
        }

        private void PreviewButton_Click(object sender, RibbonControlEventArgs e)
        {
            var previewPresenter = new PreviewPresenter();
            previewPresenter.ReplaceFields();
        }
    }
}
