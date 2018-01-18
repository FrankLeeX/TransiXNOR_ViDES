import numpy as np
import matplotlib.pyplot as plt
PLOT_FIXED_CHARGE = True
PLOT_BAND = True
PLOT_TRAN = False
PLOT_CHARGE = True
Eg = 0.252
gridx = np.genfromtxt('gridx.out')
Nx = gridx.shape[0]
gridy = np.genfromtxt("gridy.out")
## fixed charge
if (PLOT_FIXED_CHARGE):
	fn_fixed_charge = 'fixed_charge.out'
	fixed_charge = np.genfromtxt(fn_fixed_charge)
	fixed_charge = np.reshape(fixed_charge, (-1, Nx))
	print(fixed_charge.shape)
	plt.plot(gridy, fixed_charge[:,Nx/2])
	plt.show()
	
## band diagram
if (PLOT_BAND):
	fn_band_diag = 'datiout/Phi0.0.out'
	band_diag = np.genfromtxt(fn_band_diag)
	band_diag = np.reshape(band_diag, (-1, Nx))
	print(band_diag.shape)
	plt.plot(gridy, band_diag[:,Nx/2])
	plt.plot(gridy, band_diag[:,Nx/2]-Eg)
	plt.show()

if (PLOT_TRAN):
	fn_tran = 'datiout/T0.2.out'
	energy_tran = np.genfromtxt(fn_tran,delimiter=' ')
	energy_tran = energy_tran[energy_tran[:,1] > 0.0, :]
	print(energy_tran.shape)
	plt.plot(energy_tran[:,0], energy_tran[:,1])
	plt.show()

if (PLOT_CHARGE):
	fn_charge = 'datiout/ncar0.0.out'
	charge_density = np.genfromtxt(fn_charge)
	charge_density = np.reshape(charge_density, (-1, Nx))
	plt.semilogy(gridy, np.abs(charge_density[:,Nx/2]))
	plt.show()