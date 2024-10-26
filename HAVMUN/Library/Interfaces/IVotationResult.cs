using System;
using System.Collections.Generic;
using System.Text;

namespace HAVMUN.Library.Interfaces
{
    interface IVotationResult
    {
        int Agree { get; }
        int Against { get; }
        int Abstention { get; }
        float PercentOfAproval { get; }
    }
}
