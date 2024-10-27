using System;
using System.Collections.Generic;
using System.Text;

namespace HAVMUN.Library.Interfaces
{
    interface IVote
    {
        ICountry Country { get; }

        VoteValue Value { get; }
    }
}
