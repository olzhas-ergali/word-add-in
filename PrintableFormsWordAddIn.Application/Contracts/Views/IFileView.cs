using PrintableFormsWordAddIn.Application.Models;
using PrintableFormsWordAddIn.Application.Utils;
using System;
using System.Collections.Generic;

namespace PrintableFormsWordAddIn.Application.Contracts.Views
{
    public interface IFileView
    {
        void RefreshFileList(IEnumerable<PfDocument> list);
        event AsyncEventHandler Selected;
        void ShowSuccess();
        void ShowError(string message);
    }
}
