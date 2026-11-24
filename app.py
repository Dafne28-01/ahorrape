
# 1. Importamos las librerías necesarias
import streamlit as st
import pandas as pd

# 2. Configuramos el título y la presentación
st.set_page_config(page_title="Calculadora de precios")
st.title("🛍️ Calculadora de precios")
st.write("Calcula el precio final de tus productos con descuento.")

# 3. Creamos los campos para ingresar los datos
st.subheader("Datos del producto")
producto = st.text_input("Nombre del producto", "Mochila")
precio = st.number_input("Precio original (S/)", min_value=0.0, value=100.0)
descuento = st.slider("Descuento (%)", 0, 90, 20)

# 4. Realizamos los cálculos automáticamente
ahorro = precio * descuento / 100
precio_final = precio - ahorro

# 5. Mostramos los resultados principales
st.subheader("Resultado de la operación")
st.metric("Precio final", f"S/ {precio_final:.2f}")
st.metric("Dinero ahorrado", f"S/ {ahorro:.2f}")

# 6. Creamos una tabla con el resumen de la operación
datos = {
    "Concepto": ["Producto", "Precio original", "Descuento", "Ahorro", "Precio final"],
    "Valor": [producto, f"S/ {precio:.2f}", f"{descuento}%",
              f"S/ {ahorro:.2f}", f"S/ {precio_final:.2f}"]
}
tabla = pd.DataFrame(datos)

# 7. Presentamos la tabla y un mensaje final
st.subheader("Resumen de la compra")
st.dataframe(tabla, hide_index=True)
st.success("¡Cálculo realizado correctamente!")
