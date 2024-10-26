using System;
using System.Collections.Generic;
using System.Text;

namespace HAVMUN.Library.Interfaces
{
    interface IComission
    {
        int Number { get; }
        int Quorum { get; }
        List<IDelegate> Delegates { get; }
        ISecretary Secretary { get; }
    }
}
