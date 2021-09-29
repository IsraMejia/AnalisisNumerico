print(1e3) #1x10^3
print(2.5e3) # ->2500

viga = 1000 #10 metros
vigaAproximada = 1050 # medida aproximada


eAbs = abs(viga - vigaAproximada)
print(f'El error absoluto es {eAbs}')

eRelativo = eAbs / abs(viga)
print(f'El Error relativo es {eRelativo}')

eRPorcentual = eRelativo *100
print(f'El error Relativo Porcentual es {eRPorcentual}')