using PrintableFormsWordAddIn.Application.Models;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

namespace PrintableFormsWordAddIn.Application.Contracts.Services
{
    public interface IPfApiService
    {
        Task<IEnumerable<DocumentVariable>> GetDocumentVariables(Guid documentId);
        Task<IEnumerable<DocumentVariable>> GetDocumentVariablesWithValues(IEnumerable<string> ids);
        Task<Stream> GetPfDocument(Guid id);
        Task<IEnumerable<PfDocument>> GetTemplateFiles();
    }
}
