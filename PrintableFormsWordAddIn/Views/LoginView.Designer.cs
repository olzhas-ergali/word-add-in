namespace PrintableFormsWordAddIn.Views
{
    partial class LoginView
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
            this.UsernameLabel = new System.Windows.Forms.Label();
            this.UsernameTextBox = new System.Windows.Forms.TextBox();
            this.PasswordLabel = new System.Windows.Forms.Label();
            this.PasswordTextBox = new System.Windows.Forms.TextBox();
            this.LoginButton = new System.Windows.Forms.Button();
            this.CancelLoginButton = new System.Windows.Forms.Button();
            this.LoginFailLabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // UsernameLabel
            // 
            this.UsernameLabel.AutoSize = true;
            this.UsernameLabel.Location = new System.Drawing.Point(12, 9);
            this.UsernameLabel.Name = "UsernameLabel";
            this.UsernameLabel.Size = new System.Drawing.Size(80, 13);
            this.UsernameLabel.TabIndex = 0;
            this.UsernameLabel.Text = "Пользователь";
            // 
            // UsernameTextBox
            // 
            this.UsernameTextBox.Location = new System.Drawing.Point(12, 25);
            this.UsernameTextBox.Name = "UsernameTextBox";
            this.UsernameTextBox.Size = new System.Drawing.Size(327, 20);
            this.UsernameTextBox.TabIndex = 1;
            this.UsernameTextBox.TextChanged += new System.EventHandler(this.UsernameTextBox_TextChanged);
            // 
            // PasswordLabel
            // 
            this.PasswordLabel.AutoSize = true;
            this.PasswordLabel.Location = new System.Drawing.Point(12, 58);
            this.PasswordLabel.Name = "PasswordLabel";
            this.PasswordLabel.Size = new System.Drawing.Size(45, 13);
            this.PasswordLabel.TabIndex = 2;
            this.PasswordLabel.Text = "Пароль";
            // 
            // PasswordTextBox
            // 
            this.PasswordTextBox.Location = new System.Drawing.Point(12, 74);
            this.PasswordTextBox.Name = "PasswordTextBox";
            this.PasswordTextBox.Size = new System.Drawing.Size(327, 20);
            this.PasswordTextBox.TabIndex = 3;
            this.PasswordTextBox.UseSystemPasswordChar = true;
            this.PasswordTextBox.TextChanged += new System.EventHandler(this.PasswordTextBox_TextChanged);
            // 
            // LoginButton
            // 
            this.LoginButton.Location = new System.Drawing.Point(264, 131);
            this.LoginButton.Name = "LoginButton";
            this.LoginButton.Size = new System.Drawing.Size(75, 23);
            this.LoginButton.TabIndex = 4;
            this.LoginButton.Text = "Войти";
            this.LoginButton.UseVisualStyleBackColor = true;
            this.LoginButton.Click += new System.EventHandler(this.LoginButton_Click);
            // 
            // CancelLoginButton
            // 
            this.CancelLoginButton.Location = new System.Drawing.Point(183, 131);
            this.CancelLoginButton.Name = "CancelLoginButton";
            this.CancelLoginButton.Size = new System.Drawing.Size(75, 23);
            this.CancelLoginButton.TabIndex = 5;
            this.CancelLoginButton.Text = "Отмена";
            this.CancelLoginButton.UseVisualStyleBackColor = true;
            this.CancelLoginButton.Click += new System.EventHandler(this.CancelLoginButton_Click);
            // 
            // LoginFailLabel
            // 
            this.LoginFailLabel.AutoSize = true;
            this.LoginFailLabel.ForeColor = System.Drawing.SystemColors.HotTrack;
            this.LoginFailLabel.Location = new System.Drawing.Point(12, 97);
            this.LoginFailLabel.Name = "LoginFailLabel";
            this.LoginFailLabel.Size = new System.Drawing.Size(214, 13);
            this.LoginFailLabel.TabIndex = 6;
            this.LoginFailLabel.Text = "Неверное имя пользователя или пароль";
            this.LoginFailLabel.Visible = false;
            // 
            // LoginView
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(351, 166);
            this.Controls.Add(this.LoginFailLabel);
            this.Controls.Add(this.CancelLoginButton);
            this.Controls.Add(this.LoginButton);
            this.Controls.Add(this.PasswordTextBox);
            this.Controls.Add(this.PasswordLabel);
            this.Controls.Add(this.UsernameTextBox);
            this.Controls.Add(this.UsernameLabel);
            this.Name = "LoginView";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "LoginView";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label UsernameLabel;
        private System.Windows.Forms.TextBox UsernameTextBox;
        private System.Windows.Forms.Label PasswordLabel;
        private System.Windows.Forms.TextBox PasswordTextBox;
        private System.Windows.Forms.Button LoginButton;
        private System.Windows.Forms.Button CancelLoginButton;
        private System.Windows.Forms.Label LoginFailLabel;
    }
}