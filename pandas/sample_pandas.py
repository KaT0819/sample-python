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


# ['施設名', '施設名（英語）', '郵便番号', '住所', '緯度', '経度', '電話番号', 'カテゴリ１', 'カテゴリ２',
#    'FAX番号', '合計園児定員（名）', '０歳児定員（名）', '１歳児定員（名）', '２歳児定員（名）', '３歳児定員（名）',
#    '４・５歳児定員（名）', '説明（日本語）', '説明（英語）']


# 行追加　行番号指定する。
df2.loc[len(df2)] = ['追加保育園', 'add hoiku', '123-4567', '追加　住所', 0.0, 0.0, '03-1111-2222','区立保育園','認可保育園', '03-3333-4444', 100, 10, 20, 30, 40, 50, '説明（日本語）', '説明（英語）']

# 列追加　既存の行にすべて値が設定される。
df2['追加区分'] = 'ついか'
print(df2.tail(2))

# 列削除 columns指定
df3 = df2.drop(columns=['施設名（英語）', '緯度', '経度', '電話番号', 'FAX番号', '合計園児定員（名）'])
print(df3['施設名'].tail(1))
# 列削除 columns指定 内包表記で除外
df3 = df2[[col for col in df2.columns if '定員' not in col]]
print(df3['施設名'].tail(1))


# 行削除　項目と値を指定して条件にマッチしたものを抽出。否定条件にすることで除外。
df4 = df2[df2['施設名'] != 'モニカ茗荷谷']
print(df4['施設名'].tail(2))

# 行削除　インデックス指定
df4 = df4.drop(index=[1, 3, 5])
print(df4['施設名'].tail(2))
# 行削除　インデックス＝要素番号ではないので、同じインデックスを指定して2回目の削除を実行するとエラー
# df4 = df4.drop(index=[1, 3, 5])
# print(df4.tail(2))

# 文字列カラムを指定
df4.index = df4['施設名']
df4 = df4.drop(index=['追加保育園'], axis=0)
print(df4['施設名'].tail(2))


# 欠損値
print(df2.isnull().sum())

# 欠損値削除　と確認
print(df3.dropna().shape)

# 欠損値確認
print(df4[df4.isnull().any(axis=1)].head(3))
# 欠損値に値設定
df5 = df4.fillna(0)
print(df5[df5.isnull().any(axis=1)].head(3))

# データ型確認
print(df5.dtypes)

# データ型変更
df5 = df5.astype({
    '０歳児定員（名）': int,
    '１歳児定員（名）': int,
    '２歳児定員（名）': int,
    '３歳児定員（名）': int,
    '４・５歳児定員（名）': int,
})
print(df5.dtypes)
print(df5.info())

# 各行の欠損値の数確認
print(df2.isnull().sum(axis=1))
# 各列の欠損値の数確認
print(df2.isnull().sum(axis=0))


# 表結合
# names = [row for row in df2['施設名'] if '保育園' not in row]
# print(df2['施設名' == names].shape[0])
pd.merge(df2, df3, on='施設名', how='inner')

# inner: 内部結合
# left: 外部結合
# right: 右外部結合　2つ目のデータのキーをすべて残す
# outer: 完全外部結合　すべてのキーを残す
