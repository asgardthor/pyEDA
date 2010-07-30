from pyEDA.Compact.MOSParamFit import *
from pyEDA.Compact.AuroraData import *
import math
import numpy as np
from matplotlib import pyplot

# {{{
param0={
#    'ACM': 0.0 ,
#    'BINFLAG': 0 ,
    'BINUNIT': 1 ,
#    'LEVEL': 49 ,
    'MOBMOD': 1 ,
#    'PARAMCHK': 0 ,
#    'RXFLAG': 0 ,
#    'SFVTFLAG': 1 ,
#   #'STIMOD': ,
#    'TYPE': 1.0 ,
#    'VERSION': 3.2 ,
#    'VFBFLAG': 0 ,
#    'CAPMOD': 3 ,
#    'NQSMOD': 0 ,
#    'QFLAG': 0.0 ,
#    'XPART': 1.0 ,
#    'NLEV': 0 ,
#    'NOIMOD': 1 ,
#    'HDIF': 0 ,
#    'LDIF': 0 ,
    'NCH': 1.7e+17 ,
    'NGATE': 0.0,
#    'RSH': 0.0 ,
    'TOX': 129.6481e-10 ,
#   #'TOXM': ,
#   #'VGSLIM': ,
    'XJ': 0.21e-06 ,
    'XL': 0 ,
    'XW': 0 ,
#   #'DTOXCV': ,
#   #'GAMMA1': ,
#   #'GAMMA2': ,
    'NSUB': 6.0e+16 ,
    'VBM': -5.0 ,
#   #'VBX': ,
#   #'VFB': ,
    'XT': 1.55e-07 ,
    'DWB': 0.0 ,
    'DWG': 0.0 ,
    'LINT': 5e-8 ,
    'LL': 0.0 ,
    'LLN': 1.0 ,
    'LREF': 0 ,
    'LW': 0.0 ,
    'LWL': 0.0 ,
    'LWN': 1.0 ,
    'WINT': 5e-7 ,
    'WL': 0.0 ,
    'WLN': 1.0 ,
    'WREF': 0 ,
    'WW': 0.0 ,
    'WWL': 0.0 ,
    'WWN': 1.0 ,
    'DLC': 0.0 ,
    'DWC': 0.0 ,
    'LLC': 0 ,
    'LWC': 0 ,
    'LWLC': 0 ,
    'WLC': 0 ,
    'WWC': 0 ,
    'WWLC': 0 ,
    'A0': 1.0 ,
    'A1': 0.0 ,
    'A2': 1.0 ,
    'AGS': 0.0 ,
    'ALPHA0': 0.0 ,
    'ALPHA1': 0.0 ,
    'B0': 0.0 ,
    'B1': 0.0 ,
    'BETA0': 30.0 ,
    'CDSC': 2.4e-4 ,
    'CDSCB': 0.0 ,
    'CDSCD': 0.0 ,
    'CIT': 0.0 ,
    'DELTA': 0.01 ,
    'DROUT': 0.56 ,
    'DSUB': 0.56 ,
    'DVT0': 2.2 ,
    'DVT0W': 0.0 ,
    'DVT1': 0.53 ,
    'DVT1W': 5.3e+05 ,
    'DVT2': -0.032 ,
    'DVT2W': -0.032 ,
    'ETA0': 0.01 ,
    'ETAB': -0.01 ,
    'K1': 0.50 ,
    'K2': -0.0186 ,
    'K3': 80.0 ,
    'K3B': 0.0 ,
    'KETA': 0.0 ,
    'NFACTOR': 1.0 ,
    'NLX': 1.74e-07 ,
    'PCLM': 1.3 ,
    'PDIBLC1': 0.0 ,
    'PDIBLC2': 0.0001 ,
    'PDIBLCB': 0.0 ,
    'PRWB': 0.0 ,
    'PRWG': 0.0 ,
    'PSCBE1': 4.24e+08 ,
    'PSCBE2': 1.0e-05 ,
    'PVAG': 0.0 ,
    'RDSW': 1000. ,
    'U0': (600., 300., 800) ,
    'UA': (2.25e-09, -1e-8, 1e-7) ,
    'UB': (5.87e-19, 0., 1e-17) ,
    'UC': -4.65e-11 ,
    'VOFF': -0.08 ,
    'VSAT': 8.0e+04 ,
    'VTH0': (0.7, 0.1, 1),
    'W0': 2.5e-06 ,
    'WR': 1.0 ,
    'ACDE': 1 ,
#   #'CF': ,
    'CGDL': 0.0 ,
    'CGSL': 0.0 ,
    'CKAPPA': 0.6 ,
    'CLC': 0.1e-06 ,
    'CLE': 0.6 ,
    'ELM': 5.0 ,
    'MOIN': 15 ,
    'NOFF': 1 ,
    'VOFFCV': 0 ,
    'AF': 1.0 ,
    'EF': 0.0 ,
    'KF': 1.0 ,
    'NOIA': 1.0e+20 ,
    'NOIB': 5.0e+04 ,
    'NOIC': -1.4e-12 ,
    'IJTH': 0.1,
    'JS': 0.0 ,
    'JSW': 0.0 ,
    'NJ': 1.0 ,
    'RD': 0 ,
    'RS': 0 ,
    'CJ': 5.79e-04 ,
    'CJSW': 0.0 ,
    'CJSWG': 0.0 ,
    'MJ': 0.5 ,
    'MJSW': 0.33 ,
    'MJSWG': 0.33 ,
    'PB': 1.0 ,
    'PBSW': 1.0 ,
    'PBSWG': 1.0 ,
    'TNOM': 25 ,
    'AT': 3.3e+04 ,
    'KT1': 0.0 ,
    'KT1L': 0.0 ,
    'KT2': 0.022 ,
    'PRT': 0.0 ,
    'UA1': 4.31e-09 ,
    'UB1': -7.61e-18 ,
    'UC1': -5.69e-11 ,
    'UTE': -1.5 ,
    'XTI': 3.0 ,
#    'LMAX': 1.0 ,
#    'LMIN': 0.0 ,
#    'WMAX': 1.0 ,
#    'WMIN': 0.0 ,
    'LA0': 0 ,
    'LA1': 0 ,
    'LA2': 0 ,
    'LAGS': 0 ,
    'LALPHA0': 0 ,
    'LALPHA1': 0 ,
    'LBETA0': 0 ,
    'LCDSC': 0 ,
    'LCDSCB': 0 ,
    'LCDSCD': 0 ,
    'LCIT': 0 ,
    'LDELTA': 0 ,
    'LDROUT': 0 ,
    'LDSUB': 0 ,
    'LDVT0': 0 ,
    'LDVT1': 0 ,
    'LETA0': 0 ,
    'LETAB': 0 ,
    'LK': 0 ,
    'LK1': 0 ,
    'LK2': 0 ,
    'LK3': 0 ,
    'LK3B': 0 ,
    'LKETA': 0 ,
    'LNFACTOR': 0 ,
    'LNLX': 0 ,
    'LPCLM': 0 ,
    'LPDIBLC1': 0 ,
    'LPDIBLC2': 0 ,
    'LPDIBLCB': 0 ,
    'LPRWB': 0 ,
    'LPRWG': 0 ,
    'LPSCBE1': 0 ,
    'LPSCBE2': 0 ,
    'LPVAG': 0 ,
    'LRDSW': 0 ,
    'LSA0': 0 ,
    'LSB0': 0 ,
    'LSK0': 0 ,
    'LSK1': 0 ,
    'LSK2': 0 ,
    'LSL': 0 ,
    'LSW': 0 ,
    'LU0': 0 ,
    'LUA': 0 ,
    'LUB': 0 ,
    'LUC': 0 ,
    'LVOFF': 0 ,
    'LVSAT': 0 ,
    'LVTH0': 0 ,
    'LW0': 0 ,
    'LWR': 0 ,
    'PA0': 0 ,
    'PA1': 0 ,
    'PA2': 0 ,
    'PAGS': 0 ,
    'PALPHA0': 0 ,
    'PALPHA1': 0 ,
    'PBETA0': 0 ,
    'PCDSC': 0 ,
    'PCDSCB': 0 ,
    'PCDSCD': 0 ,
    'PCIT': 0 ,
    'PDELTA': 0 ,
    'PDROUT': 0 ,
    'PDSUB': 0 ,
    'PDVT0': 0 ,
    'PDVT1': 0 ,
    'PETA0': 0 ,
    'PETAB': 0 ,
    'PK1': 0 ,
    'PK2': 0 ,
    'PK3': 0 ,
    'PK3B': 0 ,
    'PKETA': 0 ,
    'PNFACTOR': 0 ,
    'PNLX': 0 ,
    'PPCLM': 0 ,
    'PPDIBLC1': 0 ,
    'PPDIBLC2': 0 ,
    'PPDIBLCB': 0 ,
    'PPRWB': 0 ,
    'PPRWG': 0 ,
    'PPSCBE1': 0 ,
    'PPSCBE2': 0 ,
    'PPVAG': 0 ,
    'PRDSW': 0 ,
    'PU0': 0 ,
    'PUA': 0 ,
    'PUB': 0 ,
    'PUC': 0 ,
    'PVOFF': 0 ,
    'PVSAT': 0 ,
    'PVTH0': 0 ,
    'PW0': 0 ,
    'PWR': 0 ,
    'WA0': 0 ,
    'WA1': 0 ,
    'WA2': 0 ,
    'WAGS': 0 ,
    'WALPHA0': 0 ,
    'WALPHA1': 0 ,
    'WBETA0': 0 ,
    'WCDSC': 0 ,
    'WCDSCB': 0 ,
    'WCDSCD': 0 ,
    'WCIT': 0 ,
    'WDELTA': 0 ,
    'WDROUT': 0 ,
    'WDSUB': 0 ,
    'WDVT0': 0 ,
    'WDVT1': 0 ,
    'WETA0': 0 ,
    'WETAB': 0 ,
    'WK1': 0 ,
    'WK2': 0 ,
    'WK3': 0 ,
    'WK3B': 0 ,
    'WKETA': 0 ,
    'WNFACTOR': 0 ,
    'WNLX': 0 ,
    'WPCLM': 0 ,
    'WPDIBLC1': 0 ,
    'WPDIBLC2': 0 ,
    'WPDIBLCB': 0 ,
    'WPRWB': 0 ,
    'WPRWG': 0 ,
    'WPSCBE1': 0 ,
    'WPSCBE2': 0 ,
    'WPVAG': 0 ,
    'WRDSW': 0 ,
    'WU0': 0 ,
    'WUA': 0 ,
    'WUB': 0 ,
    'WUC': 0 ,
    'WVOFF': 0 ,
    'WVSAT': 0 ,
    'WVTH0': 0 ,
    'WW0': 0 ,
    'WWR': 0 ,
    'LACDE': 0 ,
    'LCF': 0 ,
    'LCGDL': 0 ,
    'LCGSL': 0 ,
    'LCKAPPA': 0 ,
    'LCLC': 0 ,
    'LCLE': 0 ,
    'LMOIN': 0 ,
    'LNOFF': 0 ,
    'LVOFFCV': 0 ,
    'LRD': 0 ,
    'LRS': 0 ,
    'PRD': 0 ,
    'PRS': 0 ,
    'WRD': 0 ,
    'WRS': 0 ,
    'LAT': 0 ,
    'LKT1': 0 ,
    'LKT1L': 0 ,
    'LKT2': 0 ,
    'LPRT': 0 ,
    'LUA1': 0 ,
    'LUB1': 0 ,
    'LUC1': 0 ,
    'LUTE': 0 ,
    'PAT': 0 ,
    'PKT1': 0 ,
    'PKT1L': 0 ,
    'PKT2': 0 ,
    'PPRT': 0 ,
    'PUA1': 0 ,
    'PUB1': 0 ,
    'PUC1': 0 ,
    'PUTE': 0 ,
    'WAT': 0 ,
    'WKT1': 0 ,
    'WKT1L': 0 ,
    'WKT2': 0 ,
    'WPRT': 0 ,
    'WUA1': 0 ,
    'WUB1': 0 ,
    'WUC1': 0 ,
    'WUTE': 0,
}
# }}}


class MOSFit3(MOS_FitProject):
    def __init__(self, param0):
        super(MOSFit3, self).__init__(param0)

        print 'loading data files...'
        self.loadAuroraFile('data/level49.dat')
        print self.datasets.keys()
        print 'done.'

        # Idvg, long/wide, linear region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x15.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.1}, 'Id'))
        self.IdVg_LW_lin_b0 = dsrc

        # Idvg, mid/wide, linear region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x1p8.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.1}, 'Id'))
        self.IdVg_MW_lin_b0 = dsrc

        # Idvg, short/wide, linear region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x0p6.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.1}, 'Id'))
        self.IdVg_SW_lin_b0 = dsrc

        # Idvg, long/narrow, linear region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n1p8x15.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.1}, 'Id'))
        self.IdVg_LN_lin_b0 = dsrc

        # Idvg, short/narrow, linear region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n1p8x0p6.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':0.1}, 'Id'))
        self.IdVg_SN_lin_b0 = dsrc

        # ---
        # Idvg, long/wide, saturation region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x15.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':3.3}, 'Id'))
        self.IdVg_LW_sat_b0 = dsrc

        # Idvg, mid/wide, saturation region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x1p8.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':3.3}, 'Id'))
        self.IdVg_MW_sat_b0 = dsrc

        # Idvg, short/wide, saturation region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x0p6.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':3.3}, 'Id'))
        self.IdVg_SW_sat_b0 = dsrc

        # Idvg, long/narrow, saturation region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n1p8x15.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':3.3}, 'Id'))
        self.IdVg_LN_sat_b0 = dsrc

        # Idvg, short/narrow, saturation region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n1p8x0p6.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':3.3}, 'Id'))
        self.IdVg_SN_sat_b0 = dsrc

        # ---
        # Idvg, long/wide, Vd=1 region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x15.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':1.0}, 'Id'))
        self.IdVg_LW_d1_b0 = dsrc

        # Idvg, mid/wide, Vd=1 region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x1p8.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':1.0}, 'Id'))
        self.IdVg_MW_d1_b0 = dsrc

        # Idvg, short/wide, Vd=1 region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x0p6.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':1.0}, 'Id'))
        self.IdVg_SW_d1_b0 = dsrc

        # Idvg, long/narrow, Vd=1 region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n1p8x15.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':1.0}, 'Id'))
        self.IdVg_LN_d1_b0 = dsrc

        # Idvg, short/narrow, saturation region, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n1p8x0p6.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,    'Vds':1.0}, 'Id'))
        self.IdVg_SN_d1_b0 = dsrc

        # ---
        # IdVg, long/wide, linear region, all Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x15.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,     'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.1,   'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.2,   'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.3,   'Vds':0.1}, 'Id'))
        self.IdVg_LW_lin_ba = dsrc

        # IdVg, long/narrow, linear region, all Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n1p8x15.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,     'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.1,   'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.2,   'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.3,   'Vds':0.1}, 'Id'))
        self.IdVg_LN_lin_ba = dsrc

        # IdVg, mid/wide, linear region, all Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x1p8.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,     'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.1,   'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.2,   'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.3,   'Vds':0.1}, 'Id'))
        self.IdVg_MW_lin_ba = dsrc

        # IdVg, short/wide, linear region, all Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x0p6.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,     'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.1,   'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.2,   'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.3,   'Vds':0.1}, 'Id'))
        self.IdVg_SW_lin_ba = dsrc

        # IdVg, short/narrow, linear region, all Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n1p8x0p6.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,     'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.1,   'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.2,   'Vds':0.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.3,   'Vds':0.1}, 'Id'))
        self.IdVg_SN_lin_ba = dsrc

        #---
        # IdVg, long/wide , Vd=1, all Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x15.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,     'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.1,   'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.2,   'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.3,   'Vds':1.0}, 'Id'))
        self.IdVg_LW_d1_ba = dsrc

        # IdVg, mid/wide, Vd=1, all Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x1p8.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,     'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.1,   'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.2,   'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.3,   'Vds':1.0}, 'Id'))
        self.IdVg_MW_d1_ba = dsrc

        # IdVg, short/wide, Vd=1, all Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x0p6.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,     'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.1,   'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.2,   'Vds':1.0}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.3,   'Vds':1.0}, 'Id'))
        self.IdVg_SW_d1_ba = dsrc

        #---
        # IdVg, long/wide , saturation region, all Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x15.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,     'Vds':3.3}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.1,   'Vds':3.3}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.2,   'Vds':3.3}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.3,   'Vds':3.3}, 'Id'))
        self.IdVg_LW_sat_ba = dsrc

        # IdVg, mid/wide, saturation region, all Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x1p8.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,     'Vds':3.3}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.1,   'Vds':3.3}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.2,   'Vds':3.3}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.3,   'Vds':3.3}, 'Id'))
        self.IdVg_MW_sat_ba = dsrc

        # IdVg, short/wide, saturation region, all Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x0p6.gtr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':0.,     'Vds':3.3}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-1.1,   'Vds':3.3}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-2.2,   'Vds':3.3}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vgs', {'Vbs':-3.3,   'Vds':3.3}, 'Id'))
        self.IdVg_SW_sat_ba = dsrc

        #---
        # IdVd, long/wide , zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x15.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.9}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':1.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.7}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':3.3}, 'Id'))
        self.IdVd_LW_b0 = dsrc

        # IdVd, mid/wide , zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x1p8.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.9}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':1.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.7}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':3.3}, 'Id'))
        self.IdVd_MW_b0 = dsrc

        # IdVd, short/wide , zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n15x0p6.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.9}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':1.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.7}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':3.3}, 'Id'))
        self.IdVd_SW_b0 = dsrc

        # IdVd, long/narrow, zero Vb
        dsrc = MOS_IV_FitData()
        ds = self.datasets['n1p8x15.drr']
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':0.9}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':1.5}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.1}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':2.7}, 'Id'))
        dsrc.addCurve(ds.mosID(), ds.getCurve('Vds', {'Vbs':0.,     'Vgs':3.3}, 'Id'))
        self.IdVd_LN_b0 = dsrc

    def step10(self):
        targets=['VTH0', 'U0', 'UA', 'UB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 1')
        fit.setDataSource(1.0*self.IdVg_LW_lin_b0)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)

        return result, err


    def step20(self):
        targets=['K1', 'K2', 'UC']
        fit = MOS_IV_Fit(self.param, targets, 'Step 2')
        fit.setDataSource(1.0*self.IdVg_LW_lin_ba)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)

        return result, err


    def step30(self):
        targets = ['NFACTOR', 'VOFF']
        fit = MOS_IV_Fit(self.param, targets, 'Step 3')
        fit.setDataSource(1.0*self.IdVg_LW_lin_ba)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)

        return result, err

    def step35(self):
        targets = ['NFACTOR', 'VOFF']
        fit = MOS_IV_Fit(self.param, targets, 'Step 3-a')
        fit.setDataSource(1.0*self.IdVg_LW_lin_b0)

        fit.dataSrc.subVth=True
        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)

        return result, err


    def step40(self):
        targets = ['K3', 'W0', 'WINT', 'DWG']
        fit = MOS_IV_Fit(self.param, targets, 'Step 4')
        fit.setDataSource(self.IdVg_LW_lin_b0 + 10.0 * self.IdVg_LN_lin_b0)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)

        return result, err

    def step50(self):
        targets = ['K3B', 'DWB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 5')
        fit.setDataSource(self.IdVg_LW_lin_ba + 15.0 * self.IdVg_LN_lin_ba)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)

        return result, err

    def step70(self):
        targets = ['LINT', 'RDSW', 'DVT0', 'DVT1', 'DVT2', 'NLX']
        fit = MOS_IV_Fit(self.param, targets, 'Step 7')
        fit.setDataSource(self.IdVg_LW_lin_ba + 0.1*self.IdVg_MW_lin_ba + 0.05*self.IdVg_SW_lin_ba)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)

        return result, err

    def step80(self):
        targets = ['LINT', 'RDSW', 'PRWG']
        fit = MOS_IV_Fit(self.param, targets, 'Step 8')
        fit.setDataSource(self.IdVg_LW_lin_b0 + 0.1*self.IdVg_MW_lin_b0 + 0.05*self.IdVg_SW_lin_b0)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)

        return result, err

    def step90(self):
        targets = ['PRWB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 9')
        fit.setDataSource(self.IdVg_LW_lin_ba + 0.1*self.IdVg_MW_lin_ba + 0.05*self.IdVg_SW_lin_ba)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)

        return result, err

    def disable_step100(self):
        targets = ['DVT0W', 'DVT1W', 'RDSW', 'WR', 'PRWG']
        fit = MOS_IV_Fit(self.param, targets, 'Step 10')
        fit.setDataSource(     self.IdVg_LW_lin_ba + 
                          0.1 *self.IdVg_MW_lin_ba +
                          0.05*self.IdVg_SW_lin_ba +
                          10. *self.IdVg_LN_lin_ba +
                          2.0*self.IdVg_SN_lin_ba)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)
        return result, err

    def step110(self):
        targets = ['RDSW', 'WR', 'PRWG']
        fit = MOS_IV_Fit(self.param, targets, 'Step 11')
        fit.setDataSource(     self.IdVg_LW_lin_b0 + 
                          0.1 *self.IdVg_MW_lin_b0 +
                          0.05*self.IdVg_SW_lin_b0 +
                          10. *self.IdVg_LN_lin_b0 +
                          2.0*self.IdVg_SN_lin_b0)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)
        return result, err

    def step120(self):
        targets = ['UC', 'DWB', 'PRWB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 12')
        fit.setDataSource(     self.IdVg_LW_lin_ba + 
                          0.1 *self.IdVg_MW_lin_ba +
                          0.05*self.IdVg_SW_lin_ba +
                          10. *self.IdVg_LN_lin_ba +
                          2.0*self.IdVg_SN_lin_ba)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)
        return result, err

    def step130(self):
        targets = ['VSAT', 'A0', 'AGS']
        fit = MOS_IV_Fit(self.param, targets, 'Step 13')
        fit.setDataSource(     self.IdVd_LW_b0+ 
                          0.1 *self.IdVd_MW_b0 +
                          0.05*self.IdVd_SW_b0)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)
        return result, err

    def step132(self):
        targets = ['ETA0', 'ETAB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 13-2')
        fit.setDataSource(     self.IdVg_LW_sat_ba+ 
                          0.1 *self.IdVg_MW_sat_ba+
                          0.05*self.IdVg_SW_sat_ba+
                               self.IdVg_LW_d1_ba+ 
                          0.1 *self.IdVg_MW_d1_ba+
                          0.05*self.IdVg_SW_d1_ba)


        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)
        return result, err

    def step140(self):
        targets = ['B0', 'B1']
        fit = MOS_IV_Fit(self.param, targets, 'Step 14')
        fit.setDataSource(     self.IdVd_LW_b0+ 
                          10. *self.IdVd_LN_b0)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)
        return result, err

    def step150(self):
        targets = ['ETA0', 'DSUB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 15')
        fit.setDataSource(     self.IdVd_LW_b0+ 
                          0.1 *self.IdVd_MW_b0 +
                          0.05*self.IdVd_SW_b0)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)
        return result, err

    def step152(self):
        targets = ['ETA0', 'DSUB', 'PCLM', 'PDIBLC1', 'PDIBLC2', 'DROUT']
        fit = MOS_IV_Fit(self.param, targets, 'Step 15-2')
        fit.setDataSource(     self.IdVd_LW_b0+ 
                          0.1 *self.IdVd_MW_b0 +
                          0.05*self.IdVd_SW_b0)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)
        return result, err

    def step160(self):
        targets = ['ETA0', 'DSUB', 'PCLM', 'PDIBLC1', 'PDIBLC2', 'A1', 'A2']
        fit = MOS_IV_Fit(self.param, targets, 'Step 16')
        fit.setDataSource(     self.IdVd_LW_b0+ 
                          0.1 *self.IdVd_MW_b0 +
                          0.05*self.IdVd_SW_b0)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)
        return result, err


    def step170(self):
        targets = ['A1']
        fit = MOS_IV_Fit(self.param, targets, 'Step 17')
        fit.setDataSource(     self.IdVg_LW_sat_b0+ 
                          0.1 *self.IdVg_MW_sat_b0+
                          0.05*self.IdVg_SW_sat_b0+
                               self.IdVg_LW_d1_b0+ 
                          0.1 *self.IdVg_MW_d1_b0+
                          0.05*self.IdVg_SW_d1_b0)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)
        return result, err

    def step180(self):
        targets = ['KETA', 'ETAB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 18')
        fit.setDataSource(     self.IdVg_LW_sat_ba+ 
                          0.1 *self.IdVg_MW_sat_ba+
                          0.05*self.IdVg_SW_sat_ba+
                               self.IdVg_LW_d1_ba+ 
                          0.1 *self.IdVg_MW_d1_ba+
                          0.05*self.IdVg_SW_d1_ba)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)
        return result, err

    def step190(self):
        targets = ['KETA', 'LKETA']
        fit = MOS_IV_Fit(self.param, targets, 'Step 19')
        fit.setDataSource(     self.IdVg_LW_sat_b0+ 
                          0.1 *self.IdVg_MW_sat_b0+
                          0.05*self.IdVg_SW_sat_b0+
                               self.IdVg_LW_d1_b0+ 
                          0.1 *self.IdVg_MW_d1_b0+
                          0.05*self.IdVg_SW_d1_b0)

        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)
        return result, err

    def step200(self):
        targets = ['CDSCD']
        fit = MOS_IV_Fit(self.param, targets, 'Step 20')
        fit.setDataSource(     self.IdVg_LW_sat_b0+ 
                          0.1 *self.IdVg_MW_sat_b0+
                          0.05*self.IdVg_SW_sat_b0+
                               self.IdVg_LW_d1_b0+ 
                          0.1 *self.IdVg_MW_d1_b0+
                          0.05*self.IdVg_SW_d1_b0)

        fit.dataSrc.subVth=True
        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)

        return result, err

    def step205(self):
        targets = ['CDSCB']
        fit = MOS_IV_Fit(self.param, targets, 'Step 20-5')
        fit.setDataSource(     self.IdVg_LW_sat_ba+ 
                          0.1 *self.IdVg_MW_sat_ba+
                          0.05*self.IdVg_SW_sat_ba+
                               self.IdVg_LW_d1_ba+ 
                          0.1 *self.IdVg_MW_d1_ba+
                          0.05*self.IdVg_SW_d1_ba)

        fit.dataSrc.subVth=True
        result,err = fit.doFit(plot=pyplot)
        self.acceptParam(result, targets)

        return result, err



param0['TEMP']=25.
param0['TNOM']=25.

proj = MOSFit3(param0)
proj.run(0,199)
pyplot.show()

