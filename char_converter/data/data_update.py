import pandas as pd
import msgpack
import json

def main():
    # load data
    df_opencc_s2t = pd.read_excel('./tables/opencc_s2t.xlsx', header=None)
    df_opencc_t2s = pd.read_excel('./tables/opencc_t2s.xlsx', header=None)
    df_variants = pd.read_excel('./tables/variants.xlsx', sheet_name=0)

    variants = df_variants['yitizi'].tolist()

    df_opencc_s2t_filtered = df_opencc_s2t[~df_opencc_s2t[0].isin(variants)]
    df_opencc_t2s_filtered = df_opencc_t2s[~df_opencc_t2s[0].isin(variants)]

    df_opencc_s2t_new = pd.DataFrame(columns=['char_before', 'char_after', 'source'])
    columns = df_opencc_s2t_filtered.columns
    for i in df_opencc_s2t_filtered.index:
        yitizi = df_opencc_s2t_filtered.loc[i, 0]
        t_list = df_opencc_s2t_filtered.loc[i, 1:].dropna().tolist()
        t_str = '|'.join(t_list)
        new_row = {'char_before': yitizi, 'char_after': t_str, 'source': 'opencc_s2t'}
        df_opencc_s2t_new.loc[len(df_opencc_s2t_new)] = new_row

    df_opencc_t2s_new = pd.DataFrame(columns=['char_before', 'char_after', 'source'])
    columns = df_opencc_t2s_filtered.columns
    for i in df_opencc_t2s_filtered.index:
        yitizi = df_opencc_t2s_filtered.loc[i, 0]
        s_list = df_opencc_t2s_filtered.loc[i, 1:].dropna().tolist()
        s_str = '|'.join(s_list)
        new_row = {'char_before': yitizi, 'char_after': s_str, 'source': 'opencc_t2s'}
        df_opencc_t2s_new.loc[len(df_opencc_t2s_new)] = new_row

    # generate v2t and v2s
    df_variants_v2t = df_variants[['yitizi', 'zhengzi_t']]
    df_variants_v2t = df_variants_v2t.copy()
    df_variants_v2s = df_variants[['yitizi', 'zhengzi_s']]
    df_variants_v2s = df_variants_v2s.copy()

    df_variants_v2t_new = pd.DataFrame(columns=['char_before', 'char_after', 'source'])
    for variant in df_variants_v2t['yitizi'].unique():
        zhengzi_t_list = df_variants_v2t[df_variants_v2t['yitizi']==variant]['zhengzi_t'].tolist()
        zhengzi_t_str = '|'.join(zhengzi_t_list)
        new_row = {'char_before': variant, 'char_after': zhengzi_t_str, 'source': 'variants'}
        df_variants_v2t_new.loc[len(df_variants_v2t_new)] = new_row

    df_variants_v2s_new = pd.DataFrame(columns=['char_before', 'char_after', 'source'])
    for variant in df_variants_v2s['yitizi'].unique():
        zhengzi_s_list = df_variants_v2s[df_variants_v2s['yitizi']==variant]['zhengzi_s'].tolist()
        zhengzi_s_str = '|'.join(zhengzi_s_list)
        new_row = {'char_before': variant, 'char_after': zhengzi_s_str, 'source': 'variants'}
        df_variants_v2s_new.loc[len(df_variants_v2s_new)] = new_row

    df_variants_v2t_final = pd.concat([df_variants_v2t_new, df_opencc_s2t_new], ignore_index=True)
    df_variants_v2s_final = pd.concat([df_variants_v2s_new, df_opencc_t2s_new], ignore_index=True)

    df_variants_v2t_final.to_excel('./tables/variants_v2t.xlsx', index=False)
    df_variants_v2s_final.to_excel('./tables/variants_v2s.xlsx', index=False)


    # load dataframe
    df_v2t = pd.read_excel('./tables/variants_v2t.xlsx', sheet_name=0)
    df_v2s = pd.read_excel('./tables/variants_v2s.xlsx', sheet_name=0)

    # convert dataframe to dict
    dict_v2t = {}
    for i in df_v2t.index:
        source = df_v2t.loc[i, 'source']
        char_before = df_v2t.loc[i, 'char_before']
        char_after = df_v2t.loc[i, 'char_after']
        char_after_list = char_after.split('|')
        dict_v2t[char_before] = char_after_list

    dict_v2s = {}
    for i in df_v2s.index:
        source = df_v2s.loc[i, 'source']
        char_before = df_v2s.loc[i, 'char_before']
        char_after = df_v2s.loc[i, 'char_after']
        char_after_list = char_after.split('|')
        dict_v2s[char_before] = char_after_list

    # save dict as json
    with open("./data/v2t.json", "w") as json_file:
        json.dump(dict_v2t, json_file)
    with open("./data/v2s.json", "w") as json_file:
        json.dump(dict_v2s, json_file)

    # convert dict to MessagePack and save
    msgpack_file = './data/v2t.msgpack'
    data = dict_v2t
    with open(msgpack_file, 'wb') as f:
        packed_data = msgpack.packb(data, use_bin_type=True)
        f.write(packed_data)
    msgpack_file = './data/v2s.msgpack'
    data = dict_v2s
    with open(msgpack_file, 'wb') as f:
        packed_data = msgpack.packb(data, use_bin_type=True)
        f.write(packed_data)

if __name__ == '__main__':
    main()