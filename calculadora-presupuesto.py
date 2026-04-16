# =============================================
# Calculadora de Presupuesto Personal
# Autor: Luis Fernando Capacoila Copa
# Semana 1 - Nivel 0 Python
# =============================================

print("=" * 50)
print("CALCULADORA PRESUPUESTO PERSONAL".center(50))
print("=" * 50)
print()

# INGRESOS
print("INGRESOS")
print("=" * 50)
print()

sueldo = float(input("ingrese su sueldo mensual (S/.): "))
pago_extra = float(input("ingrese su ingreso extra (S/.): "))
#EL INGRESO EXTRA ES SI ES QUE TIENES SINO PONLE 0

total_ingreso = sueldo + pago_extra

# GASTOS
print()
print("GASTOS MENSUALES")
print("=" * 50)
print()

alquiler = float(input("ingrese el pago de alquiler mensual(S/.): "))
comida = float(input("ingrese el gasto en comida mensual(S/.): "))
transporte = float(input("ingrese el gasto mensual en transporte(S/.): "))
servicios = float(input("gastos mensuales en agua,luz,internet(S/:): "))
educacion = float(input("pago mensual en estudios(S/.): "))
otros = float(input("otros gastos mensuales(S/.): "))

total_gasto = alquiler + comida + transporte + servicios + educacion + otros

# CÁLCULOS
print()
saldo = total_ingreso - total_gasto
porcentaje_gasto = (total_gasto/total_ingreso) * 100 if total_ingreso > 0 else 0
porcentaje_ahorro = (saldo/total_ingreso) * 100 if total_ingreso > 0 else 0

# --- REPORTE ---
print()
print("=" * 50)
print("RESUMEN DEL MES".center(50))
print("=" * 50)
print(f"{'Total ingresos':<25} S/ {total_ingreso}")
print(f"{'Total gastos':<25} S/ {total_gasto}")
print("-" * 50)
print(f"{'Saldo disponible':<25} S/ {saldo}")
print()
print(f"{'Gastas el':<25} {porcentaje_gasto}% de tu ingreso")
print(f"{'Ahorras el':<25} {porcentaje_ahorro}% de tu ingreso")
print()

# DIAGNÓSTICO
print("-" * 50)
print("  DIAGNÓSTICO".center(50))
print("-" * 50)

if porcentaje_ahorro >= 20:
    print("  Excelente. Ahorras mas del 20%, vas muy bien.")
elif porcentaje_ahorro >= 10:
    print("  Bien. Ahorras algo, pero puedes mejorar.")
elif porcentaje_ahorro > 0:
    print("  Cuidado. Ahorras poco, revisa tus gastos.")
else:
    print("  Alerta. Gastas mas de lo que ganas.")

print()

# --- META INVERSIÓN EN APRENDIZAJE ---
inversion = float(input("¿Cuánto puedes invertir en aprendizaje/mes? (S/): "))
meses_nivel0 = 3
costo_total  = inversion * meses_nivel0

print()
print("=" * 50)
print("PLAN DE INVERSIÓN EN TU CARRERA".center(50))
print("=" * 50)
print(f"{'Inversión mensual':<25} S/ {inversion}")
print(f"{'Costo total Nivel 0':<25} S/ {costo_total}")
print(f"{'Saldo tras invertir':<25} S/ {saldo - inversion}")
print()
print(f"  Recuerda: estudiar con Claude es gratis.")
print(f"  Tu mayor inversion es tiempo, no dinero.")
print("=" * 50)



