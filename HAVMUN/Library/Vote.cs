using System;
using System.Collections.Generic;
using System.Text;
using HAVMUN.Library.Interfaces;

namespace HAVMUN.Library
{
    class Vote : IVote
    {
        public ICountry Country { get; }

        public VoteValue Value { get; }

        public Vote(ICountry country, VoteValue value)
        {
            Country = country;
            Value = value;
        }
    }
}
