using PrintableFormsWordAddIn.Application.Contracts.Views;
using PrintableFormsWordAddIn.Application.Utils;
using System;
using System.Windows.Forms;

namespace PrintableFormsWordAddIn.Views
{
    public partial class LoginView : Form, ILoginView
    {
        public LoginView()
        {
            InitializeComponent();
        }

        public event AsyncEventHandler Login;
        public string Username { get; private set; }
        public string Password { get; private set; }

        public void ShowError(string message)
        {
            LoginFailLabel.Text = message;
            LoginFailLabel.Visible = true;
        }

        public void ShowSuccess()
        {
            this.DialogResult = DialogResult.OK;
            this.Close();
        }

        private void LoginButton_Click(object sender, EventArgs e)
        {
            Login.Invoke(sender, e);
        }

        private void CancelLoginButton_Click(object sender, EventArgs e)
        {
            this.DialogResult = DialogResult.Cancel;
            this.Close();
        }

        private void PasswordTextBox_TextChanged(object sender, EventArgs e)
        {
            this.Password = PasswordTextBox.Text;
            LoginFailLabel.Visible = false;
        }

        private void UsernameTextBox_TextChanged(object sender, EventArgs e)
        {
            this.Username = UsernameTextBox.Text;
            LoginFailLabel.Visible = false;
        }
    }
}
