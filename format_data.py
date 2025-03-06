import json
from datetime import datetime

# 原始数据
data = {
    "rows": [
        {"cumulative_unique_addresses": 257447, "transaction_date": "2024-08-29", "unique_addresses": 257447},
        # ... 这里是完整的数据
    ]
}

def create_sql_table():
    # 创建表的 SQL 语句
    create_table_sql = """
CREATE TABLE IF NOT EXISTS unique_addresses (
    transaction_date DATE,
    unique_addresses BIGINT,
    cumulative_unique_addresses BIGINT,
    PRIMARY KEY (transaction_date)
);
"""
    
    # 插入数据的 SQL 语句
    insert_sql = "INSERT INTO unique_addresses (transaction_date, unique_addresses, cumulative_unique_addresses) VALUES\n"
    
    # 格式化每一行数据
    values = []
    for row in data["rows"]:
        values.append(f"('{row['transaction_date']}', {row['unique_addresses']}, {row['cumulative_unique_addresses']})")
    
    # 组合完整的 SQL 语句
    final_sql = create_table_sql + insert_sql + ",\n".join(values) + ";"
    
    # 将 SQL 语句写入文件
    with open("unique_addresses.sql", "w") as f:
        f.write(final_sql)
    
    print("SQL file has been created successfully!")

if __name__ == "__main__":
    create_sql_table() 