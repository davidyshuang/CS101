import numpy as np

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    plt = None
    MATPLOTLIB_AVAILABLE = False
    print("Warning: matplotlib not available. Visualization functionality will be disabled.")

def get_positional_encoding(pos, d_model, T=10000):
    """
    计算给定位置和模型维度的位置编码
    
    参数:
    pos: 位置索引 (从0开始)
    d_model: 模型维度 (必须是偶数)
    T: 频率基数，默认为10000
    
    返回:
    PE: 位置编码向量，形状为(d_model,)
    """
    # 创建位置编码向量
    PE = np.zeros(d_model)
    
    # 对于每个维度i
    for i in range(d_model):
        # 计算频率参数
        if i % 2 == 0:  # 偶数维度使用正弦
            div_term = np.power(T, (2 * (i // 2)) / d_model)
            PE[i] = np.sin(pos / div_term)
        else:  # 奇数维度使用余弦
            div_term = np.power(T, (2 * (i // 2)) / d_model)
            PE[i] = np.cos(pos / div_term)
            
    return PE

# 新增：演示周期和波长的概念
def demonstrate_period_vs_wavelength():
    """
    演示周期和波长的概念差异
    """
    print("=== 周期和波长的概念演示 ===")
    print("在数学函数中:")
    print("- 周期(T)是指函数重复自身的间隔")
    print("- 波长(λ)通常指物理波中相邻波峰之间的距离")
    print("- 在位置编码的上下文中，我们关注的是函数值重复的间隔")
    print()
    
    # 展示不同频率参数的影响
    positions = np.arange(0, 50, 0.1)
    
    # 高频情况 (频率参数小)
    freq_param_small = 1.0
    sine_small = np.sin(positions / freq_param_small)
    
    # 低频情况 (频率参数大)
    freq_param_large = 10.0
    sine_large = np.sin(positions / freq_param_large)
    
    print(f"对于 sin(pos/{freq_param_small}):")
    print(f"  - 频率参数: {freq_param_small}")
    print(f"  - 周期: 2π * {freq_param_small} = {2*np.pi*freq_param_small:.2f}")
    print()
    
    print(f"对于 sin(pos/{freq_param_large}):")
    print(f"  - 频率参数: {freq_param_large}")
    print(f"  - 周期: 2π * {freq_param_large} = {2*np.pi*freq_param_large:.2f}")
    print()
    
    print("结论:")
    print("- 频率参数越大，函数振荡越慢(周期越长)")
    print("- 频率参数越小，函数振荡越快(周期越短)")

# 新增：分析频率和波长的变化
def analyze_frequency_and_wavelength(d_model=8, T=10000):
    """
    分析位置编码中频率和波长如何随维度变化
    """
    print("=== 频率和波长分析 ===")
    print(f"模型维度: {d_model}")
    print(f"频率基数 T: {T}")
    print()
    
    for i in range(d_model):
        # 计算频率参数（角频率）
        k = i // 2
        # 角频率 ω = 1 / T^(2k/d_model)
        angular_freq = 1 / (T ** (2 * k / d_model))
        # 周期 T = 2π / ω = 2π * T^(2k/d_model)
        period = 2 * np.pi * (T ** (2 * k / d_model))
        
        func_type = "正弦" if i % 2 == 0 else "余弦"
        print(f"维度 {i:2d} ({func_type}): 角频率 = {angular_freq:.2e}, 周期 = {period:.2f}")

# 示例计算
print("=== Transformer位置编码计算示例 ===\n")

# 设置较小的维度以便展示 (实际中常用512或1024)
d_model = 8
print(f"模型维度: {d_model}")

# 计算前几个位置的编码
for pos in range(5):
    pe = get_positional_encoding(pos, d_model)
    print(f"位置 {pos} 的编码向量:")
    print(f"  {pe}")
    print()

# 展示特定维度上的值变化
print("=== 查看特定维度上的值如何随位置变化 ===")
dims_to_show = [0, 1, 2, 3]  # 显示前4个维度
positions = range(10)  # 查看前10个位置

for dim in dims_to_show:
    values = []
    for pos in positions:
        pe = get_positional_encoding(pos, d_model)
        values.append(pe[dim])
    print(f"维度 {dim}: {' '.join([f'{v:7.4f}' for v in values])}")

print("\n=== 频率参数计算示例 ===")
print("对于d_model=8的情况:")
for i in range(d_model):
    if i % 2 == 0:
        k = i // 2
        freq = 10000 ** (2 * k / d_model)
        print(f"维度 {i} (正弦): 频率参数 = 10000^(2*{k}/{d_model}) = {freq:.2f}")

# 调用新增的演示函数
demonstrate_period_vs_wavelength()
print()

# 调用新增的分析函数
analyze_frequency_and_wavelength(d_model)

# 可视化位置编码
def visualize_positional_encoding(max_positions=50, d_model=64):
    """
    可视化位置编码矩阵
    """
    if not MATPLOTLIB_AVAILABLE:
        print("Visualization skipped: matplotlib not available.")
        return
        
    plt.figure(figsize=(12, 6))
    
    # 创建位置编码矩阵
    pe_matrix = np.zeros((max_positions, d_model))
    for pos in range(max_positions):
        pe_matrix[pos, :] = get_positional_encoding(pos, d_model)
    
    # 绘制热力图
    plt.imshow(pe_matrix, cmap='RdBu', aspect='auto')
    plt.colorbar(label='编码值')
    plt.xlabel('维度')
    plt.ylabel('位置')
    plt.title('位置编码可视化 (前50个位置, 64维)')
    plt.tight_layout()
    plt.savefig('/Users/huangyunsheng/projects/CS101/positional_encoding_visualization.png')
    plt.close()

# 生成可视化图表
if MATPLOTLIB_AVAILABLE:
    visualize_positional_encoding()
    print("\n已生成位置编码可视化图表: positional_encoding_visualization.png")
else:
    print("\n跳过可视化: 未安装 matplotlib")