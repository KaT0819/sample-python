#!/usr/bin/env python
import pandas as pd

# CSV読み込み
df1 = pd.read_csv('hoikuen.csv', encoding='shift_jis')
print(df1.head(3))

# データ型の確認
print(df1.dtypes)

# 特定の列をインデックスとして読み込む
df1 = pd.read_csv('hoikuen.csv', encoding='shift_jis', index_col='No.')

# 読み込みカラム指定
df1 = pd.read_csv('hoikuen.csv', encoding='shift_jis', usecols=['施設名', '０歳児定員（名）', '２歳児定員（名）'])

print(df1.head(3))

# df2 = pd.read_excel('hoikuen.xlsx', encoding='shift_jis')
# df2.head(3)


df2 = pd.read_csv('hoikuen.csv', encoding='shift_jis', index_col='No.')

# value_counts：特定のカラムについてカウント（normalize=Trueとすると割合で返す）
print(df2['合計園児定員（名）'].value_counts())
print(df2['合計園児定員（名）'].value_counts(normalize=True))

# unique：特定カラムの値のリストを返す。
print(df2['合計園児定員（名）'].unique())

# 定員60名以上の園の合計を算出
sum = sum([1 for d in df2['合計園児定員（名）'].unique() if d >= 60])
print(sum)

# 行数,列数
print(df2.shape)

# 要素数(行数 x 列数)
print(df2.size)

# 列名取得
print(df2.columns)

# ソート
# print(df2.sort_values(by='合計園児定員（名）', ascending=False).head(3))

# ソート　インデックス降り直し（drop=True　元のインデックスを除去）
# print(df2.sort_values(by='合計園児定員（名）', ascending=False).reset_index(drop=True).head(3))

# ソート　インデックス降り直し（na_position='first'欠損値を先頭に）
# print(df2.sort_values(by='０歳児定員（名）', ascending=False, na_position='first').reset_index(drop=True).head(3))

# 複数条件ソート
print(df2.sort_values(by=['カテゴリ１', 'カテゴリ２'], ascending=[True, True], na_position='first').head(3))


# ['施設名', '施設名（英語）', '郵便番号', '住所', '緯度', '経度', '電話番号', 'カテゴリ１', 'カテゴリ２',
#    'FAX番号', '合計園児定員（名）', '０歳児定員（名）', '１歳児定員（名）', '２歳児定員（名）', '３歳児定員（名）',
#    '４・５歳児定員（名）', '説明（日本語）', '説明（英語）']

# 列指定取得
print(df2[['施設名', '合計園児定員（名）']])

# 行指定取得（例は１行目と9行目）
print(df2.iloc[[0,9]])
# 行指定取得（例は１行目と9行目、0番目と4番目）
print(df2.iloc[[0,9], [0,3]])

# 行指定取得（例は2行目から4行目）
print(df2.iloc[1:3])

# 取り出し方による型の違い
print(type(df2.iloc[0]))
print(type(df2.iloc[[0,9]]))


# 行指定取得
print(df2.loc[1])

cols = list(df2.columns)
cols.remove('カテゴリ１')
cols.remove('カテゴリ２')
# 公私区分と認可区分
# print(df2[cols])

ser3 = df2.iloc[3][['施設名', 'カテゴリ１']]
print(type(df2.loc[3]))
print(ser3)


# 条件式（120名以上）
print(len(df2[df2['合計園児定員（名）'] >= 120]))

# 複数条件式（１つの条件をカッコでくくる）
print(len(df2[(df2['合計園児定員（名）'] >= 120) & (df2['０歳児定員（名）'] >= 9)]))

# ~はnot（施設名列に保育園を含む値を抽出）
print(df2[~df2['施設名'].str.contains('保育園')].shape[0])

print(len(df2[df2['カテゴリ２'].str.contains('認定こども園')]))
# 完全一致なら==でもよい
print(len(df2[df2['カテゴリ２']=='認定こども園']))

print(len(df2[df2['施設名'].str.contains('文京')]))

# グルーピング
# 件数
print(df2.groupby('カテゴリ２').count())
# 平均
print(df2.groupby('カテゴリ２').mean())
# 合計
print(df2.groupby('カテゴリ２').sum())
# 最大
print(df2.groupby('カテゴリ２').max('合計園児定員（名）'))
# 最小
print(df2.groupby('カテゴリ２').min('合計園児定員（名）'))
# 平均　複数項目指定
print(df2.groupby(['カテゴリ１', 'カテゴリ２']).mean())

# 一括取得
print(df2.groupby(['カテゴリ１', 'カテゴリ２']).agg(['count','max', 'min', 'sum'])['合計園児定員（名）'])

# 統計情報取得（すべての項目がほしい時はinclude='all'）
# print(df2.describe(include='all'))
print(df2.describe())

print(df2.describe().loc['mean']['０歳児定員（名）'])
