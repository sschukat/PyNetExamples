namespace UILibrary
{
    partial class MainForm
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
            this.buttonCallPython = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // buttonCallPython
            // 
            this.buttonCallPython.Location = new System.Drawing.Point(12, 12);
            this.buttonCallPython.Name = "buttonCallPython";
            this.buttonCallPython.Size = new System.Drawing.Size(75, 23);
            this.buttonCallPython.TabIndex = 0;
            this.buttonCallPython.Text = "Call Python";
            this.buttonCallPython.UseVisualStyleBackColor = true;
            this.buttonCallPython.Click += new System.EventHandler(this.ButtonCallPython_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(245, 44);
            this.Controls.Add(this.buttonCallPython);
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "MainForm";
            this.Text = "TestWinforms";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button buttonCallPython;
    }
}

