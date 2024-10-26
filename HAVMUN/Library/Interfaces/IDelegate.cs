using System;
using System.Collections.Generic;
using System.Text;

namespace HAVMUN.Library.Interfaces
{
    interface IDelegate : IMember
    {
        ICountry _Country { get; }
    }
}
