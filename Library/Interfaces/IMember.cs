using System;
using System.Collections.Generic;
using System.Text;

namespace HAVMUN.Library.Interfaces
{
    interface IMember
    {
        IComission _Comission { get; }
        string AccessCode { get; }
    }
}
