using System;
using System.Collections.Generic;
using System.Text;

namespace HAVMUN.Library.Interfaces
{
    interface IVotation
    {
        bool Open { get; }
        IComission _Comission { get; }
        string Topic { get; }
        List<IVote> Votes { get; }
        void ReceiveVote (IVote vote);
        IVotationResult EndVotation();
    }
}
