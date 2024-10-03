import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='darkgrid')

# Nama file dataset
orders_file = 'orders_dataset.csv'
order_items_file = 'order_items_dataset.csv'

# Load datasets
try:
    orders_df = pd.read_csv(orders_file)
    order_items_df = pd.read_csv(order_items_file)
    st.write("Dataset 'orders_dataset.csv' dan 'order_items_dataset.csv' berhasil dimuat.")
except Exception as e:
    st.error(f"Gagal memuat dataset: {e}")
    st.stop()

# Menampilkan 5 baris pertama dari setiap dataset
st.write("5 Baris Pertama dari Dataset Orders:")
st.write(orders_df.head())

st.write("5 Baris Pertama dari Dataset Order Items:")
st.write(order_items_df.head())

# Merge datasets on 'order_id'
try:
    merged_df = pd.merge(orders_df, order_items_df, on='order_id')
except KeyError as e:
    st.error(f"Error menggabungkan dataset: {e}")
    st.stop()

# Convert 'order_purchase_timestamp' to datetime
merged_df['order_purchase_timestamp'] = pd.to_datetime(merged_df['order_purchase_timestamp'])

# Menampilkan 5 baris pertama dari merged data
st.write("5 Baris Pertama dari Data yang Digabungkan:")
st.write(merged_df.head())

# Mengecek tipe data
st.write("Informasi Dataset:")
st.write(merged_df.info())

# Mengecek data yang hilang
st.write("Jumlah Data yang Hilang di Setiap Kolom:")
st.write(merged_df.isnull().sum())

# Menghapus baris dengan missing values jika diperlukan
merged_df.dropna(inplace=True)

# Membuat kolom 'month_year' untuk analisis bulanan
merged_df['month_year'] = merged_df['order_purchase_timestamp'].dt.to_period('M')

# Group by 'month_year' dan sum kolom 'price'
sales_per_month = merged_df.groupby('month_year')['price'].sum()

# Visualisasi tren penjualan per bulan
st.subheader("Tren Penjualan per Bulan")
plt.figure(figsize=(12, 6))
sns.lineplot(x=sales_per_month.index.to_timestamp(), y=sales_per_month.values, marker='o', color='blue')
plt.title('Tren Penjualan Bulanan')
plt.xlabel('Bulan')
plt.ylabel('Total Penjualan')
st.pyplot(plt)

# Visualisasi sederhana menggunakan Streamlit (opsional untuk tes)
st.line_chart(sales_per_month)

# Menghitung produk terlaris berdasarkan penjualan
top_products = merged_df.groupby('product_id').agg({'price': 'sum'}).nlargest(5, 'price')

# Menampilkan produk terlaris
st.subheader("5 Produk Terlaris Berdasarkan Total Penjualan")
st.write(top_products)

# Visualisasi 5 produk terlaris
plt.figure(figsize=(10, 6))
top_products['price'].plot(kind='bar', color='green')
plt.title('Top 5 Produk Terlaris')
plt.xlabel('Product ID')
plt.ylabel('Total Penjualan')
st.pyplot(plt)

# Visualisasi sederhana menggunakan Streamlit (opsional untuk tes)
st.bar_chart(top_products['price'])

st.caption('By: Amalina Shabrina')
