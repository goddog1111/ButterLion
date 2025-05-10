import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import load_data
from pathlib import Path

# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 建立 figures 資料夾
figures_dir = Path('figures')
figures_dir.mkdir(exist_ok=True)

def analyze_numeric_columns(df):
    """分析數值型欄位"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    stats = df[numeric_cols].describe()
    return stats

def analyze_categorical_columns(df):
    """分析類別型欄位"""
    categorical_cols = df.select_dtypes(include=['object']).columns
    stats = {}
    for col in categorical_cols:
        stats[col] = df[col].value_counts()
    return stats

def create_visualizations(df):
    """建立視覺化圖表"""
    # 數值型欄位的分布圖
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x=col)
        plt.title(f'{col} 分布圖')
        plt.savefig(f'figures/{col}_distribution.png')
        plt.close()

    # 類別型欄位的長條圖
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        plt.figure(figsize=(12, 6))
        value_counts = df[col].value_counts().head(10)  # 只顯示前10個類別
        sns.barplot(x=value_counts.index, y=value_counts.values)
        plt.title(f'{col} 前10個類別分布')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'figures/{col}_distribution.png')
        plt.close()

def generate_markdown_report(df, numeric_stats, categorical_stats):
    """生成 Markdown 報告"""
    report = """# 資料分析報告

## 資料概覽
"""
    report += f"- 資料筆數：{len(df)}\n"
    report += f"- 欄位數量：{len(df.columns)}\n"
    report += f"- 欄位名稱：{', '.join(df.columns)}\n\n"

    report += "## 數值型欄位統計\n"
    report += numeric_stats.to_markdown()
    report += "\n\n"

    report += "## 類別型欄位統計\n"
    for col, stats in categorical_stats.items():
        report += f"### {col}\n"
        report += stats.head(10).to_markdown()  # 只顯示前10個類別
        report += "\n\n"

    report += "## 視覺化圖表\n"
    # 數值型欄位的分布圖
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        report += f"### {col} 分布圖\n"
        report += f"![{col} 分布圖](figures/{col}_distribution.png)\n\n"

    # 類別型欄位的長條圖
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        report += f"### {col} 前10個類別分布\n"
        report += f"![{col} 分布圖](figures/{col}_distribution.png)\n\n"

    # 寫入報告
    with open('analysis_report.md', 'w', encoding='utf-8') as f:
        f.write(report)

def main():
    # 載入資料
    df = load_data()
    
    # 進行分析
    numeric_stats = analyze_numeric_columns(df)
    categorical_stats = analyze_categorical_columns(df)
    
    # 建立視覺化
    create_visualizations(df)
    
    # 生成報告
    generate_markdown_report(df, numeric_stats, categorical_stats)
    print("分析報告已生成：analysis_report.md")

if __name__ == "__main__":
    main() 