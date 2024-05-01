import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

'''サンプルコード１'''
### データフレームを表示するだけのシンプルなコードです.
# データ生成部
st.write('### 1. CSVデータを生成して、テーブル表示する')
filename = 'sample.csv'
num_data = st.number_input('生成するデータの行数', min_value=1, value=3)# データ数(行数)
if st.button(f'{filename}を生成'):
    # データ生成
    df = pd.DataFrame({
    '日付': pd.date_range(start='2021-01-01', periods=num_data, freq='D'),
    '温度': np.random.rand(num_data) * 30,  # 温度 (0から30の間でランダム)
    '湿度': np.random.randint(40, 100, size=num_data)  # 湿度 (40%から100%の間でランダム)
    })
    # CSVに保存
    df.to_csv(filename, index=False)
    # メッセージ表示
    st.write(f'{filename}を生成しただぬ')

# CSVデータの読み込み
data = pd.read_csv(filename)

# DataFrameを画面に表示
st.write(data)


'''サンプルコード２'''
### 編集可能なデータフレームを表示して、編集結果を表示するコードです。
st.write("### 2. 編集可能なテーブルを表示し、結果をグラフ化する")
edited_data = st.data_editor(data, num_rows=10) #ここで編集結果を取得している

# 編集結果を表示
fig = px.line(edited_data, x='日付', y='温度', title='温度の時系列データ', markers=True)
st.plotly_chart(fig)


'''サンプルコード３'''
st.write("### 3. 編集結果をインタラクティブなグラフで可視化する")

fig = go.Figure()
fig.add_trace(go.Scatter(x=edited_data['日付'], 
                         y=edited_data['温度'], 
                         mode='lines+markers', 
                         name='温度', 
                         line=dict(color='red')
                         ))
fig.add_trace(go.Scatter(x=edited_data['日付'], 
                         y=edited_data['湿度'], 
                         mode='lines+markers', 
                         name='湿度', 
                         line=dict(color='blue'), 
                         yaxis='y2' # 第二軸を指定
                         )) 

# X軸, Y軸の設定
fig.update_layout(
    # グラフのタイトル
    title='温度と湿度の時系列データ',
    # X軸
    xaxis=dict(
        showgrid=False, # x軸のグリッドを非表示
        showline=True, # x軸のラインを表示
        ticks='inside', # x軸の目盛りを内側に表示
        tickcolor='black', # x軸の目盛りの色
    ),
    # Y軸
    yaxis=dict(
        title='温度 [℃]', # y軸のタイトル
        showgrid=False, # y軸のグリッドを非表示
        showline=True, # y軸のラインを表示
        ticks='inside', # y軸の目盛りを内側に表示
        tickcolor='black', # y軸の目盛りの色
    ),
    # 第二軸
    yaxis2=dict(
        title='湿度 [%]', # 第二軸のタイトル
        overlaying='y', # y軸と重ねる
        side='right', # 右側に表示
        showgrid=False, # y軸のグリッドを非表示
        showline=True, # y軸のラインを表示
        ticks='inside', # y軸の目盛りを内側に表示
        tickcolor='black', # y軸の目盛りの色
    )
)

st.plotly_chart(fig) # チャート描画