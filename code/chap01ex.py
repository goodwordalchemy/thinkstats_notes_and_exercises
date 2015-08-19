"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

from collections import defaultdict
import numpy as np
import sys
import nsfg

import thinkstats2


def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    """Reads the NSFG Respondents data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    # CleanFemResp(df)
    return df

def getCountFromPregFile():
	preg_df = nsfg.ReadFemPreg()
	nsfg.CleanFemPreg(preg_df)
	preg_map = nsfg.MakePregMap(preg_df)

	pregnums = defaultdict(int)
	for i,c in enumerate(preg_map):
		pregnums[len(pregmap[c])] += 1
	print("from pregfile:")
	print(pregnums)



# def CleanFemResp(df):
#     """Recodes variables from the Responents frame.

#     df: DataFrame
#     """

#     # birthwgt_lb contains at least one bogus value (51 lbs)
#     # replace with NaN
#     df.birthwgt_lb[df.birthwgt_lb > 20] = np.nan
    
#     # replace 'not ascertained', 'refused', 'don't know' with NaN
#     na_vals = [97, 98, 99]
#     df.birthwgt_lb.replace(na_vals, np.nan, inplace=True)
#     df.birthwgt_oz.replace(na_vals, np.nan, inplace=True)
#     df.hpagelb.replace(na_vals, np.nan, inplace=True)

#     df.babysex.replace([7, 9], np.nan, inplace=True)
#     df.nbrnaliv.replace([9], np.nan, inplace=True)

#     # birthweight is stored in two columns, lbs and oz.
#     # convert to a single column in lb
#     # NOTE: creating a new column requires dictionary syntax,
#     # not attribute assignment (like df.totalwgt_lb)
#     df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0    

#     # due to a bug in ReadStataDct, the last variable gets clipped;
#     # so for now set it to NaN
#     df.cmintvw = np.nan




def main():

    df = ReadFemResp()

    count = df.pregnum.value_counts().sort_index()
    print(count)

    getCountFromPregFile()

if __name__ == '__main__':
    main()
