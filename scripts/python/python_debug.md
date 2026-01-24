# 作为Python调试新手，在VS Code中配置和使用调试功能可能会感到有些复杂。别担心，这份指南将从零开始，逐步带你掌握在VS Code中调试Python脚本的完整流程。无论你是在Windows、macOS还是Linux系统上，都能找到适合你的操作方法

作为 Python 调试新手，在 VS Code 中配置和使用调试功能可能会感到有些复杂。别担心，这份指南将从零开始，逐步带你掌握在 VS Code 中调试 Python 脚本的完整流程。无论你是在 Windows、macOS 还是 Linux 系统上，都能找到适合你的操作方法。

## 一、环境配置：搭建 VS Code Python 调试基础

### 1.1 安装 VS Code 和 Python 扩展

首先，你需要确保已经安装了 VS Code 编辑器。如果还没有安装，可以访问[VS Code 官网](https://code.visualstudio.com/)下载适合你操作系统的版本。安装过程非常简单，按照提示一步步操作即可。

安装好 VS Code 后，我们需要安装 Python 扩展。这个扩展是微软官方开发的，为 VS Code 提供了强大的 Python 开发和调试功能。安装步骤如下：



1. 打开 VS Code，点击左侧活动栏中的**扩展图标**（看起来像四个小方块），或者使用快捷键`Ctrl+Shift+X`（Windows/Linux）或`Cmd+Shift+X`（macOS）[(1)](https://blog.csdn.net/gitblog_09283/article/details/142225234)。

2. 在搜索框中输入 "Python"，你会看到由 Microsoft 提供的官方 Python 扩展。这个扩展通常排在搜索结果的第一位，图标是一个蓝色的 Python 标志[(1)](https://blog.csdn.net/gitblog_09283/article/details/142225234)。

3. 点击扩展旁边的**安装**按钮。安装过程可能需要一些时间，安装完成后，你会看到安装按钮变成了一个设置图标（⚙️），或者显示 "禁用" 和 "卸载" 两个按钮。

4. 安装完成后，建议关闭并重新打开 VS Code，以确保 Python 扩展被正确识别。

### 1.2 选择 Python 解释器

Python 扩展安装完成后，你需要选择一个 Python 解释器。解释器是运行 Python 代码的环境，VS Code 需要知道使用哪个 Python 版本来执行和调试你的代码。

选择 Python 解释器的方法有两种：

**方法一：通过状态栏选择**



1. 在 VS Code 窗口的右下角，你会看到一个显示当前 Python 解释器的区域。如果这是你第一次使用 VS Code，这里可能显示 "Python 3.12.0 64-bit" 或类似内容，或者显示 "Select Python Interpreter"。

2. 点击这个区域，会弹出一个列表，显示系统中所有可用的 Python 解释器。

3. 选择你想要使用的 Python 版本。如果列表中没有你需要的解释器，可以点击 "Enter interpreter path..." 手动输入路径。

**方法二：通过命令面板选择**



1. 使用快捷键`Ctrl+Shift+P`（Windows/Linux）或`Cmd+Shift+P`（macOS）打开命令面板[(5)](https://blog.csdn.net/siliconscribe/article/details/147497719)。

2. 在命令面板中输入 "Python: Select Interpreter"，然后选择这个命令。

3. 在弹出的列表中选择你需要的 Python 解释器。

选择解释器后，VS Code 会在你的工作区设置文件（settings.json）中添加一行配置：



```
"python.pythonPath": "C:/Python312/python.exe"  # Windows示例

"python.pythonPath": "/usr/local/bin/python3"   # macOS/Linux示例
```

### 1.3 配置虚拟环境（可选但推荐）

虚拟环境是 Python 开发中的最佳实践，它允许你为不同的项目创建独立的 Python 环境，避免依赖包之间的冲突。在 VS Code 中配置虚拟环境非常简单：



1. **创建虚拟环境**：

* 在 VS Code 的集成终端中（使用快捷键`Ctrl+`\` 打开），输入以下命令创建一个名为`.venv`的虚拟环境：



```
python -m venv .venv
```



* 等待虚拟环境创建完成。

1. **激活虚拟环境**：

* Windows 系统：使用命令`.venv\Scripts\activate`

* macOS/Linux 系统：使用命令`.venv/bin/activate`[(8)](https://blog.csdn.net/datadragon/article/details/147521832)

1. **在 VS Code 中选择虚拟环境**：

* 虚拟环境创建后，VS Code 会自动检测到它。你可以通过 "Python: Select Interpreter" 命令选择`.venv`目录下的 Python 解释器[(10)](https://docs.posit.co/ide/server-pro/user/vs-code/guide/python-environments.html)。

1. **调试时使用虚拟环境**：

* 如果你希望调试时使用虚拟环境，需要在`launch.json`文件中配置`python`属性，指定虚拟环境的解释器路径[(14)](https://m.php.cn/faq/1743663.html)：



```
"python": "\${workspaceFolder}/.venv/bin/python"  # macOS/Linux

"python": "\${workspaceFolder}\\\\.venv\\\Scripts\\\python.exe"  # Windows
```

### 1.4 配置调试文件 launch.json

现在我们需要创建一个调试配置文件`launch.json`，这个文件告诉 VS Code 如何启动和调试你的 Python 程序。

**创建 launch.json 文件的步骤**：



1. 点击 VS Code 左侧活动栏中的**调试图标**（看起来像一个播放按钮），或者使用快捷键`Ctrl+Shift+D`。

2. 在调试视图中，你会看到一个 "创建一个 launch.json 文件" 的链接。点击这个链接[(62)](https://vscode.github.net.cn/docs/python/debugging)。

3. 选择调试配置类型。在弹出的菜单中，选择 "Python 文件" 或 "Python: Current File"[(62)](https://vscode.github.net.cn/docs/python/debugging)。

4. VS Code 会自动在你的工作区根目录下创建一个`.vscode`文件夹，并在其中生成`launch.json`文件。

**launch.json 基础配置说明**：

以下是一个典型的`launch.json`配置文件内容：



```
{

&#x20; "version": "0.2.0",

&#x20; "configurations": \[

&#x20;   {

&#x20;     "name": "Python: Current File",

&#x20;     "type": "python",

&#x20;     "request": "launch",

&#x20;     "program": "\${file}",

&#x20;     "console": "integratedTerminal"

&#x20;   }

&#x20; ]

}
```

各配置项的含义：



* **name**：调试配置的名称，显示在调试配置下拉菜单中

* **type**：调试器类型，这里固定为 "python"

* **request**：调试请求类型，"launch" 表示启动调试，"attach" 表示附加到已运行的进程

* **program**：要调试的 Python 文件路径。`${file}`表示当前打开的文件

* **console**：指定调试时使用的控制台类型。"integratedTerminal" 表示使用 VS Code 的集成终端，"internalConsole" 表示使用内部调试控制台[(5)](https://blog.csdn.net/siliconscribe/article/details/147497719)

### 1.5 常见环境配置问题解决

在配置过程中，你可能会遇到一些常见问题：

**问题 1：VS Code 找不到 Python 解释器**



* 确保 Python 已安装并添加到系统路径中

* 尝试重启 VS Code

* 使用 "Python: Restart Language Server" 命令（通过`Ctrl+Shift+P`打开命令面板）[(4)](https://blog.csdn.net/functionflow1/article/details/147521551)

**问题 2：虚拟环境无法激活**



* 在 Windows 系统中，如果遇到 "Activate.ps1 is not digitally signed" 的错误，可以在 PowerShell 中运行以下命令临时更改执行策略：



```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

注意：这只是临时设置，不会永久改变系统策略

**问题 3：Python 扩展版本不兼容**



* 从 2024 年起，最新的 Python 扩展不再支持 Python 3.8 及以下版本[(68)](https://wenku.csdn.net/answer/1pgdkge9ax)

* 如果需要调试 Python 3.7 或更低版本，你需要安装旧版本的 Python 扩展

* 建议升级 Python 到 3.9 或更高版本以获得最佳支持[(75)](https://blog.csdn.net/jst100/article/details/125783925)

## 二、调试基础流程：从断点到变量查看

### 2.1 设置断点

断点是调试的基础，它告诉调试器在代码的特定位置暂停执行，以便你检查程序状态。在 VS Code 中设置断点非常简单：

**设置普通断点**：



1. 打开你要调试的 Python 文件

2. 在代码编辑器中，找到你想要程序暂停的代码行

3. 点击该行号左侧的灰色边缘区域，会出现一个**红色圆点**，表示断点已设置[(18)](https://blog.51cto.com/u_16175509/12754554)

4. 再次点击红点可以移除断点[(26)](https://blog.csdn.net/linnaa6/article/details/145418572)

**设置条件断点**：

条件断点只有在特定条件满足时才会触发，这在调试循环或复杂逻辑时特别有用。设置方法：



1. 先设置一个普通断点（红色圆点）

2. 右键单击断点红点，选择 "编辑断点" 或 "添加条件断点"[(41)](https://code.visualstudio.com/docs/debugtest/debugging)

3. 在弹出的输入框中输入条件表达式，例如`i == 100`或`name == "Alice"`[(44)](https://blog.51cto.com/u_16213364/12710222)

4. 只有当条件表达式为`true`时，断点才会触发

**设置日志断点（Logpoints）**：

日志断点不会暂停程序执行，但会在调试控制台输出一条消息，这对于监控变量值变化而不中断程序特别有用：



1. 右键单击行号区域，选择 "添加日志点"[(52)](https://blog.csdn.net/Saki_Python/article/details/132469700)

2. 输入日志消息，使用花括号`{}`包裹要输出的变量或表达式，例如：



```
"Value of x: {x}, iteration: {i}"
```



1. 日志断点显示为菱形图标，程序执行到此处时会在调试控制台输出指定消息

### 2.2 启动调试

设置好断点后，就可以启动调试了。有几种方法可以启动调试：

**方法一：使用调试工具栏**



1. 确保你已经在调试视图中（`Ctrl+Shift+D`）

2. 在调试配置下拉菜单中选择你需要的配置（如 "Python: Current File"）

3. 点击绿色的**播放按钮**（F5）启动调试

**方法二：使用编辑器运行按钮**



1. 在编辑器右上角，你会看到一个运行按钮（▶️）

2. 点击按钮旁边的下拉箭头，选择 "调试 Python 文件"

**方法三：使用快捷键**

直接按下`F5`键，VS Code 会使用默认的调试配置启动调试[(3)](https://cloud.tencent.cn/developer/article/2562202)

**启动调试后的界面变化**：



* VS Code 界面会发生变化，显示调试相关的面板

* 编辑器顶部会出现调试工具栏

* 左侧会显示变量、监视、调用栈等调试信息面板

* 程序会执行到第一个断点处暂停，断点行号会有黄色背景高亮显示

### 2.3 执行控制：单步调试技巧

程序在断点处暂停后，你可以使用调试工具栏或快捷键来控制程序的执行：

**调试工具栏按钮说明**（从左到右）：



1. **继续 / 暂停**（F5）：继续执行程序，直到遇到下一个断点或程序结束

2. **单步跳过**（F10）：执行当前行代码，不进入函数调用

3. **单步进入**（F11）：进入函数调用内部

4. **单步跳出**（Shift+F11）：从当前函数返回到调用处

5. **重新启动**（Ctrl+Shift+F5）：重新开始调试会话

6. **停止**（Shift+F5）：停止调试会话[(37)](https://blog.51cto.com/u_16213462/13194794)

**单步调试的使用场景**：



* **F10 单步跳过**：当你想执行当前行但不想进入函数内部时使用。例如，当你确定某个函数是正确的，只想观察调用后的结果。

* **F11 单步进入**：当你想查看某个函数内部的执行过程时使用。这在调试自定义函数或第三方库时特别有用。

* **Shift+F11 单步跳出**：当你已经进入一个函数但想快速返回到调用处时使用。例如，你进入了一个辅助函数，但发现这里没有问题，想回到主逻辑继续调试。

**调试过程中的代码导航**：



* 调试过程中，可以在编辑器中自由导航查看代码

* 黄色箭头指示当前执行位置

* 你可以通过点击其他行来改变执行路径（但需要谨慎使用，可能导致程序状态不一致）

### 2.4 查看变量和调试信息

调试的核心是查看程序运行时的状态，VS Code 提供了多种方式来查看变量和调试信息：

**Variables（变量）面板**：



* 调试启动后，左侧会自动显示 Variables 面板

* 显示当前作用域内的所有变量，包括局部变量、全局变量和函数参数

* 变量值会随着代码执行实时更新

* 你可以展开列表查看复杂对象（如列表、字典、类实例）的详细内容[(30)](https://ask.csdn.net/questions/8329424)

**Watch（监视）面板**：



* Watch 面板允许你添加自定义表达式进行监控

* 点击 Watch 面板中的 \*\*+\*\* 号，输入变量名或表达式，如`my_list[0]`或`len(my_dict)`

* 表达式会在每次程序暂停时自动计算并显示结果

* 你可以添加多个监视表达式，方便跟踪关键变量的变化[(30)](https://ask.csdn.net/questions/8329424)

**快速查看变量值**：



* 在编辑器中，将鼠标悬停在变量上，可以快速查看变量值

* 对于复杂对象，会显示一个预览框，你可以展开查看更多细节[(33)](https://blog.51cto.com/u_16175488/13108523)

**调试控制台（Debug Console）**：



* 调试控制台允许你在调试过程中执行 Python 代码

* 你可以直接输入表达式计算值，修改变量，调用函数等

* 例如，你可以输入`print(my_variable)`来查看变量内容，或者输入`my_list.append(42)`来修改变量

**调用栈（Call Stack）面板**：



* 显示当前的函数调用栈

* 点击栈中的某个调用，可以查看该层级的变量作用域

* 这在调试递归函数或多层函数调用时特别有用

### 2.5 调试过程中的变量修改

在调试过程中，你可以临时修改变量值，这对于测试不同的输入条件或验证假设非常有用：

**修改变量值的方法**：



1. 在 Variables 或 Watch 面板中，双击要修改的变量值

2. 输入新的值，按回车键确认

3. 变量值会立即更新，程序后续的执行将使用新值[(38)](https://m.php.cn/faq/1626767.html)

**注意事项**：



* 修改变量值只在当前调试会话中有效，不会影响源代码

* 谨慎修改变量，可能导致程序状态不一致

* 建议在修改变量前先理解变量的用途和依赖关系

## 三、调试技巧和高级功能

### 3.1 条件断点的高级应用

条件断点不仅可以使用简单的表达式，还可以使用更复杂的逻辑：

**使用复合条件**：

你可以使用 Python 的逻辑运算符创建复杂条件：



```
i > 100 and i < 200  # 在i在100到200之间时触发

name.startswith("A")  # 当name以A开头时触发

type(obj) is list     # 当obj是列表类型时触发
```

**使用函数调用**：

条件表达式中可以调用函数，这为条件断点提供了极大的灵活性：



```
is\_prime(number)  # 当number是素数时触发（需要先定义is\_prime函数）
```

**命中次数条件**：

除了表达式条件，你还可以设置断点在被命中特定次数后触发：



1. 右键单击断点，选择 "编辑断点"

2. 在输入框中选择 "Hit Count" 选项

3. 输入触发条件，如：

* `==10`：第 10 次命中时触发

* `>=5`：第 5 次及以后命中时触发

* `%10==0`：每 10 次命中触发一次

### 3.2 日志断点（Logpoints）的使用技巧

日志断点是一个强大但容易被忽视的功能，它特别适合以下场景：

**监控循环变量**：

在循环中使用日志断点可以实时查看循环变量的变化，而不会中断程序执行：



```
"Loop iteration {i}, total={total}"
```

**跟踪函数调用**：

在函数入口处设置日志断点，可以记录函数的参数：



```
"Function 'calculate' called with args: {args}, kwargs: {kwargs}"
```

**记录关键状态**：

在程序的关键节点设置日志断点，记录重要的状态信息：



```
"Reached critical section with status: {status}, value: {value}"
```

### 3.3 调试命令行参数

很多 Python 程序需要接收命令行参数，在 VS Code 中调试带参数的程序很简单：

**在 launch.json 中配置参数**：

在调试配置中添加`args`属性，指定命令行参数：



```
{

&#x20; "name": "Python: With Arguments",

&#x20; "type": "python",

&#x20; "request": "launch",

&#x20; "program": "\${file}",

&#x20; "args": \["--input", "data.csv", "--output", "result.txt", "--verbose"]

}
```

**动态输入参数**：

如果你需要每次调试时输入不同的参数，可以使用以下方法：



1. 在代码中使用`input()`函数获取用户输入

2. 调试时，在集成终端中输入参数

3. 注意：使用`console`属性指定为 "integratedTerminal"，这样才能在终端中输入内容

**传递环境变量**：

如果程序需要特定的环境变量，可以在`launch.json`中配置`env`属性：



```
{

&#x20; "name": "Python: With Environment",

&#x20; "type": "python",

&#x20; "request": "launch",

&#x20; "program": "\${file}",

&#x20; "env": {

&#x20;   "API\_KEY": "your\_api\_key\_here",

&#x20;   "DEBUG\_MODE": "true"

&#x20; }

}
```

### 3.4 调试技巧总结

**快速定位问题的技巧**：



1. **二分查找法**：在大型程序中，可以在中间位置设置断点，判断问题出现在前半部分还是后半部分，逐步缩小范围。

2. **条件断点精准定位**：使用条件断点只在特定条件下触发，避免在无关的代码处反复暂停。

3. **日志断点辅助调试**：在不适合设置断点的地方（如生产环境代码），使用日志断点记录关键信息。

**调试复杂数据结构**：



* 使用`pprint`模块格式化输出复杂对象

* 在调试控制台中使用 Python 的内置函数（如`dir()`、`help()`）查看对象信息

* 对于自定义类，考虑实现`__str__`或`__repr__`方法，以便在调试时显示有意义的信息

**性能调试技巧**：



* 使用日志断点记录关键代码段的执行时间

* 在循环中使用条件断点（如每 100 次触发一次），避免性能开销

* 调试完成后，及时删除或禁用不需要的断点

## 四、常见调试场景实战

### 4.1 调试循环问题

循环是编程中最容易出错的地方之一，以下是调试循环的常用方法：

**场景 1：无限循环**



* 在循环内部设置断点

* 使用条件断点设置循环次数上限，如`i > 1000`时触发

* 检查循环条件是否永远为真

* 确保循环变量在每次迭代中都有变化

**场景 2：循环变量错误**



* 使用日志断点输出循环变量的值：



```
"Iteration {i}: x = {x}, y = {y}"
```



* 在 Watch 面板中添加循环变量，实时跟踪变化

* 检查循环变量的初始值和更新逻辑

**场景 3：列表 / 字典处理错误**



* 使用调试控制台打印列表或字典的内容

* 检查索引是否越界

* 使用`enumerate`函数同时获取索引和值，方便调试：



```
for i, item in enumerate(items):

&#x20;   \# 在这设置断点，i和item都会显示在Variables面板中
```

### 4.2 调试函数调用问题

**场景 1：函数返回错误结果**



* 在函数入口处设置断点，检查参数是否正确

* 在函数返回前设置断点，查看返回值是否符合预期

* 使用 Watch 面板跟踪函数内部的关键变量

* 检查函数内部的计算逻辑

**场景 2：函数未被调用**



* 在函数定义处设置断点（断点显示为菱形，表示函数断点）

* 检查调用函数的条件是否满足

* 使用调试控制台验证函数是否存在（检查命名空间）

**场景 3：递归函数调试**



* 使用条件断点限制递归深度，避免栈溢出

* 记录递归调用的参数和层次：



```
"Recursion depth {depth}, arguments: {args}"
```



* 检查递归终止条件是否正确

### 4.3 调试条件判断错误

**场景 1：条件判断总是为真或假**



* 在条件表达式上设置断点

* 使用调试控制台计算条件表达式的结果

* 检查变量类型是否正确（如`==` vs `is`的区别）

* 注意 Python 的布尔值转换规则（如空字符串、0、空列表都被视为 False）

**场景 2：多个条件组合错误**



* 使用括号明确条件优先级

* 在每个子条件处设置日志断点，输出中间结果

* 逐步构建复杂条件，确保每个部分都按预期工作

### 4.4 调试异常和错误

**场景 1：程序崩溃（抛出异常）**



* VS Code 会在异常发生时自动暂停，显示异常信息

* 在异常堆栈中找到出错的代码行

* 使用调试工具查看异常发生时的变量状态

* 注意异常的类型和错误信息，这通常能直接告诉你问题所在

**场景 2：捕获异常但处理不当**



* 在`except`块中设置断点，查看异常信息

* 确保异常处理代码能够正确处理所有可能的异常类型

* 使用`traceback`模块打印完整的异常堆栈信息

**场景 3：逻辑错误（没有异常但结果错误）**



* 这种错误最难调试，因为程序正常运行但输出错误

* 在关键计算步骤设置断点，检查中间结果

* 使用日志断点记录关键变量的值变化

* 考虑使用单元测试来验证各个功能点

## 五、VS Code 调试功能进阶

### 5.1 调试配置的高级选项

除了基础的调试配置，`launch.json`还有许多高级选项可以让调试更加灵活：

`justMyCode`**选项**：

这个选项控制是否只调试用户代码，默认值为`true`。当设置为`false`时，可以进入第三方库的代码进行调试，这在排查库本身的问题时非常有用[(64)](https://blog.csdn.net/weixin_44212848/article/details/142684478)：



```
{

&#x20; "name": "Python: Debug Library Code",

&#x20; "type": "python",

&#x20; "request": "launch",

&#x20; "program": "\${file}",

&#x20; "justMyCode": false

}
```

`stopOnEntry`**选项**：

设置为`true`时，调试器会在程序的第一行代码处暂停，而不管是否有断点。这在调试脚本的初始执行时很有用[(58)](https://donjayamanne.github.io/pythonVSCodeDocs/docs/debugging/)：



```
{

&#x20; "name": "Python: Start at First Line",

&#x20; "type": "python",

&#x20; "request": "launch",

&#x20; "program": "\${file}",

&#x20; "stopOnEntry": true

}
```

`autoReload`**选项**：

启用自动重载功能后，当你在调试过程中修改了代码，调试器会自动重新加载代码。这在开发过程中非常方便，不需要每次修改都重新启动调试：



```
{

&#x20; "name": "Python: Auto Reload",

&#x20; "type": "python",

&#x20; "request": "launch",

&#x20; "program": "\${file}",

&#x20; "autoReload": {

&#x20;   "enable": true

&#x20; }

}
```

### 5.2 多文件项目调试

当调试包含多个文件的项目时，需要特别注意以下几点：

**设置正确的工作目录**：

使用`cwd`属性指定工作目录，这样相对路径才能正确解析：



```
{

&#x20; "name": "Python: Project Debug",

&#x20; "type": "python",

&#x20; "request": "launch",

&#x20; "program": "\${workspaceFolder}/main.py",

&#x20; "cwd": "\${workspaceFolder}"

}
```

**调试模块而非脚本**：

如果项目使用模块结构，可以使用`module`属性指定要调试的模块，而不是直接指定文件：



```
{

&#x20; "name": "Python: Debug Module",

&#x20; "type": "python",

&#x20; "request": "launch",

&#x20; "module": "my\_package.my\_module",

&#x20; "args": \["--option", "value"]

}
```

**处理导入路径问题**：



* 确保`PYTHONPATH`包含项目根目录

* 在`launch.json`中配置环境变量，设置`PYTHONPATH`：



```
{

&#x20; "name": "Python: With Path",

&#x20; "type": "python",

&#x20; "request": "launch",

&#x20; "program": "\${file}",

&#x20; "env": {

&#x20;   "PYTHONPATH": "\${workspaceFolder}"

&#x20; }

}
```

### 5.3 调试性能优化

虽然 VS Code 本身的调试功能很强大，但过度使用可能会影响程序性能。以下是一些优化建议：

**减少断点数量**：



* 只保留必要的断点

* 使用条件断点代替多个普通断点

* 调试完成后及时删除不需要的断点

**使用轻量级调试工具**：



* 优先使用日志断点而非普通断点

* 在生产环境代码中，使用`print`语句配合条件判断，避免性能开销

* 对于性能敏感的代码，可以考虑使用分析器而非调试器

**分批调试**：



* 将大型程序分成多个部分调试

* 先确保核心功能正确，再调试边缘情况

* 使用单元测试覆盖主要功能点

### 5.4 调试扩展推荐

VS Code 的扩展生态系统非常丰富，以下是一些对调试有帮助的扩展：

**Python 相关扩展**：



1. **Python Extension Pack**：包含多个 Python 开发工具，如 Pylance（智能感知）、Python Debugger 等

2. **Python Environment Manager**：帮助管理多个 Python 环境和虚拟环境

3. **Code Runner**：可以快速运行 Python 代码片段，无需配置调试环境

**通用调试工具**：



1. **CodeLLDB**：强大的调试器，支持多种编程语言

2. **Rainbow CSV**：以颜色编码显示 CSV 文件，方便调试数据处理程序

3. **vscode-icons**：为不同文件类型显示不同图标，提高文件识别效率

## 六、VS Code 版本兼容性说明

在使用 VS Code 调试 Python 时，版本兼容性是一个需要注意的问题：

### 6.1 Python 版本要求

**VS Code Python 扩展的 Python 版本支持**：



* 从 2024 年起，最新的 Python 扩展不再支持 Python 3.8 及以下版本[(68)](https://wenku.csdn.net/answer/1pgdkge9ax)

* 最低支持 Python 3.7 版本，但建议使用 3.9 或更高版本[(75)](https://blog.csdn.net/jst100/article/details/125783925)

* 对于 Python 3.7，需要安装较旧版本的 Python 扩展（2020.11 或更早）[(73)](https://wenku.csdn.net/answer/4xfj9u5fbo)

**Python 扩展版本与 VS Code 版本对应关系**：



* Python 扩展 2024.14.0 要求 VS Code 版本 1.91.0 或更高[(70)](https://wenku.csdn.net/answer/1yep2hxoxf)

* 确保你的 VS Code 是最新版本，以获得最佳的扩展支持

* 可以在扩展页面查看具体的版本要求

### 6.2 操作系统兼容性

VS Code 的 Python 调试功能在不同操作系统上的表现基本一致，但有一些细微差别：

**Windows 系统注意事项**：



* 路径使用反斜杠（`\`），需要转义或使用原始字符串

* 虚拟环境激活脚本在`.venv\Scripts`目录下

* 某些系统命令（如`which`）在 Windows 上不可用

**macOS 系统注意事项**：



* 系统自带的 Python 版本可能较旧，建议安装最新版本

* 使用 Homebrew 等包管理器安装 Python 比较方便

* 注意文件权限问题，某些系统目录需要管理员权限

**Linux 系统注意事项**：



* 通常预装了 Python，但版本可能不是最新

* 需要确保`python3`命令指向正确的版本

* 包管理系统（如 apt、yum）可以方便地安装 Python 和依赖包

### 6.3 故障排除指南

**常见错误及解决方法**：



1. **"找不到 Python 解释器" 错误**

* 确保 Python 已安装并添加到系统路径

* 重启 VS Code 和 Python 语言服务器

* 手动指定 Python 解释器路径

1. **"调试器无法连接" 错误**

* 检查防火墙设置，确保调试端口（默认 5678）未被阻止

* 如果使用虚拟环境，确保调试配置中指定了正确的解释器路径

* 尝试重新安装 Python 扩展

1. **"断点未命中" 问题**

* 检查断点是否设置在可执行代码行上

* 确保代码文件已保存

* 尝试重新加载断点（使用 "重新应用所有断点" 命令）

1. **性能问题**

* 减少断点数量

* 使用条件断点和日志断点

* 关闭不必要的扩展

* 升级硬件或使用更轻量级的编辑器

## 结语

通过这份详细的指南，相信你已经掌握了在 VS Code 中调试 Python 脚本的基本技能。从环境配置到断点设置，从变量查看到手动态修改，这些技能将大大提升你的编程效率和问题解决能力。

**最后的建议**：



1. **实践出真知**：多写代码，多调试，在实践中积累经验。

2. **循序渐进**：从简单的程序开始调试，逐步挑战复杂的项目。

3. **善用工具**：VS Code 提供了丰富的调试功能，花时间探索这些功能会带来巨大回报。

4. **保持耐心**：调试是编程中不可避免的环节，保持耐心和细心，总能找到问题所在。

记住，每个优秀的程序员都是从调试中成长起来的。随着经验的积累，你会越来越熟练地使用这些调试技巧，甚至能够快速定位和解决复杂的问题。祝你编程愉快！

**参考资料&#x20;**

\[1] 【保姆级超详细还免费】VSCode Python 扩展安装与配置指南-CSDN博客[ https://blog.csdn.net/gitblog\_09283/article/details/142225234](https://blog.csdn.net/gitblog_09283/article/details/142225234)

\[2] Python on Visual Studio Code[ https://vscode-docs1.readthedocs.io/en/latest/languages/python/](https://vscode-docs1.readthedocs.io/en/latest/languages/python/)

\[3] VS Code Python配置完全指南:从安装到调试的初学者教程-腾讯云开发者社区-腾讯云[ https://cloud.tencent.cn/developer/article/2562202](https://cloud.tencent.cn/developer/article/2562202)

\[4] 手把手教你用vscode打造python开发环境(保姆级教程)[ https://blog.csdn.net/functionflow1/article/details/147521551](https://blog.csdn.net/functionflow1/article/details/147521551)

\[5] VS Code配置Python环境全攻略(手把手保姆级教程)\_vs python配置-CSDN博客[ https://blog.csdn.net/siliconscribe/article/details/147497719](https://blog.csdn.net/siliconscribe/article/details/147497719)

\[6] 在 Visual Studio Code 中调试 Python 应用程序的配置\_Vscode中文网[ https://vscode.github.net.cn/docs/python/debugging](https://vscode.github.net.cn/docs/python/debugging)

\[7] 10分钟搞定!VS Code配置Python开发环境指南(2025新版)本文将手把手教你如何在VSCode中配置Pyth - 掘金[ https://juejin.cn/post/7502442616072519743](https://juejin.cn/post/7502442616072519743)

\[8] 手把手教你用VSCode打造Python开发环境(含避坑指南)\_vscode 运行python 带环境变量-CSDN博客[ https://blog.csdn.net/datadragon/article/details/147521832](https://blog.csdn.net/datadragon/article/details/147521832)

\[9] Using Python environments in VS Code[ https://vscode-docs-arc.readthedocs.io/en/latest/python/environments/](https://vscode-docs-arc.readthedocs.io/en/latest/python/environments/)

\[10] Python Environments in VS Code[ https://docs.posit.co/ide/server-pro/user/vs-code/guide/python-environments.html](https://docs.posit.co/ide/server-pro/user/vs-code/guide/python-environments.html)

\[11] 在Visual Code中启用virtualenv\_在vscode中启用virtualenv-CSDN博客[ https://blog.csdn.net/yiifaa/article/details/78815568](https://blog.csdn.net/yiifaa/article/details/78815568)

\[12] vscode python debug venv\_Visual Studio Code Python开发调试环境设置-CSDN博客[ https://blog.csdn.net/weixin\_39931146/article/details/112990408](https://blog.csdn.net/weixin_39931146/article/details/112990408)

\[13] vscode launch.json配置python路径-VSCode-PHP中文网[ https://m.php.cn/faq/1396663.html](https://m.php.cn/faq/1396663.html)

\[14] VSCode Python开发\_虚拟环境与包管理深度配置-VSCode-PHP中文网[ https://m.php.cn/faq/1743663.html](https://m.php.cn/faq/1743663.html)

\[15] VSCode Python 项目调试完全指南VSCode Python 项目调试完全指南 问题背景 在使用 VSCode - 掘金[ https://juejin.cn/post/7431371798866001930](https://juejin.cn/post/7431371798866001930)

\[16] Vscode 开发 Python 的一些基础设置\_51CTO博客\_vscode开发python项目[ https://blog.51cto.com/u\_4948298/13805492](https://blog.51cto.com/u_4948298/13805492)

\[17] 使用vscode打造python开发环境\_program": "\${workspacefolder} 可以设置多个入口吗-CSDN博客[ https://blog.csdn.net/qq\_39852676/article/details/106555881](https://blog.csdn.net/qq_39852676/article/details/106555881)

\[18] vscode设置断点Python\_mob649e8166858d的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16175509/12754554](https://blog.51cto.com/u_16175509/12754554)

\[19] Easy Guide to Debugging Python in VS Code for Beginners[ https://toxigon.com/how-to-debug-python-in-vscode-for-beginners](https://toxigon.com/how-to-debug-python-in-vscode-for-beginners)

\[20] Mastering Advanced Python Debugging in VSCode in Simple Steps[ https://toxigon.com/advanced-python-debugging-in-vscode](https://toxigon.com/advanced-python-debugging-in-vscode)

\[21] visual studio code python 断点\_mob64ca12e36a1d的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16213377/13041045](https://blog.51cto.com/u_16213377/13041045)

\[22] Debugging[ https://vscode-docs-arc.readthedocs.io/en/latest/editor/debugging/](https://vscode-docs-arc.readthedocs.io/en/latest/editor/debugging/)

\[23] 调试 Python 代码，设置断点，检查代码 - Visual Studio (Windows) | Microsoft Learn[ https://learn.microsoft.com/zh-cn/visualstudio/python/debugging-python-in-visual-studio?view=vs-2022](https://learn.microsoft.com/zh-cn/visualstudio/python/debugging-python-in-visual-studio?view=vs-2022)

\[24] VSCode 设置断点Python\_mob64ca12f0cf8f的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16213433/13066345](https://blog.51cto.com/u_16213433/13066345)

\[25] 如何在 VS Code 中调试 Python 代码?\_vscode python 调试-CSDN博客[ https://blog.csdn.net/2503\_90908880/article/details/146246666](https://blog.csdn.net/2503_90908880/article/details/146246666)

\[26] 如何使用 VS Code 的调试工具进行断点调试\_vscode断点怎么用-CSDN博客[ https://blog.csdn.net/linnaa6/article/details/145418572](https://blog.csdn.net/linnaa6/article/details/145418572)

\[27] VSCode怎么断点调试Python\_VSCode配置Python调试与断点使用教程-VSCode-PHP中文网[ https://m.php.cn/faq/1482023.html](https://m.php.cn/faq/1482023.html)

\[28] Python程序员Visual Studio Code指南\_visual studio code python-CSDN博客[ https://blog.csdn.net/Saki\_Python/article/details/132469700](https://blog.csdn.net/Saki_Python/article/details/132469700)

\[29] Python\_leetcode怎么调试-CSDN博客[ https://blog.csdn.net/2401\_87990658/article/details/145347830](https://blog.csdn.net/2401_87990658/article/details/145347830)

\[30] VSCode调试Python时如何实时查看变量值?\_编程语言-CSDN问答[ https://ask.csdn.net/questions/8329424](https://ask.csdn.net/questions/8329424)

\[31] Why debugging Python in VS Code feels like having a superpower[ https://www.toxigon.com/debugging-python-with-vs-code](https://www.toxigon.com/debugging-python-with-vs-code)

\[32] vscode python 断点 设置 表达式\_mob64ca12e1497a的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16213368/11777165](https://blog.51cto.com/u_16213368/11777165)

\[33] vs code python 看变量插件\_mob649e8161738c的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16175488/13108523](https://blog.51cto.com/u_16175488/13108523)

\[34] VSCODE调试查看变量\_VSCode调试变量查看技巧\_ - CSDN文库[ https://wenku.csdn.net/answer/47p8n6qp5v](https://wenku.csdn.net/answer/47p8n6qp5v)

\[35] 在vscode中运行Python程序时，显示变量值 - CSDN文库[ https://wenku.csdn.net/answer/6jcc455mq7](https://wenku.csdn.net/answer/6jcc455mq7)

\[36] Python调试进阶之路:从入门到精通VSCode断点与变量监视(附实战案例)-CSDN博客[ https://blog.csdn.net/VarChat/article/details/154354948](https://blog.csdn.net/VarChat/article/details/154354948)

\[37] 怎么调试vscode python\_mob64ca12f7ae31的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16213462/13194794](https://blog.51cto.com/u_16213462/13194794)

\[38] VSCode调试:断点与变量监控指南-VSCode-PHP中文网[ https://m.php.cn/faq/1626767.html](https://m.php.cn/faq/1626767.html)

\[39] Python代码使用vscode调试时看到所有变量的值\_mob64ca12f062df的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16213431/12945962](https://blog.51cto.com/u_16213431/12945962)

\[40] Python程序员Visual Studio Code指南\_visual studio code python-CSDN博客[ https://blog.csdn.net/Saki\_Python/article/details/132469700](https://blog.csdn.net/Saki_Python/article/details/132469700)

\[41] Debug code with Visual Studio Code[ https://code.visualstudio.com/docs/debugtest/debugging](https://code.visualstudio.com/docs/debugtest/debugging)

\[42] VS Code Debugging: Pro Tips & Tricks for Faster Coding[ https://toxigon.com/vs-code-debugging-tips-and-tricks](https://toxigon.com/vs-code-debugging-tips-and-tricks)

\[43] VSCode调试技巧:条件断点实战-VSCode-PHP中文网[ https://m.php.cn/faq/1625174.html](https://m.php.cn/faq/1625174.html)

\[44] python vscode 条件断点表达式怎么写\_mob64ca12e04e7a的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16213364/12710222](https://blog.51cto.com/u_16213364/12710222)

\[45] VSCode调试:Python程序调试技巧-VSCode-PHP中文网[ https://m.php.cn/faq/1632187.html](https://m.php.cn/faq/1632187.html)

\[46] Python调试进阶之路:从入门到精通VSCode断点与变量监视(附实战案例)-CSDN博客[ https://blog.csdn.net/VarChat/article/details/154354948](https://blog.csdn.net/VarChat/article/details/154354948)

\[47] Mastering Python Debugging in VSCode[ https://toxigon.com/how-to-make-the-most-of-your-python-debugger-in-vscode](https://toxigon.com/how-to-make-the-most-of-your-python-debugger-in-vscode)

\[48] 调试 Python 代码，设置断点，检查代码 - Visual Studio (Windows) | Microsoft Learn[ https://learn.microsoft.com/zh-cn/visualstudio/python/debugging-python-in-visual-studio?view=vs-2022](https://learn.microsoft.com/zh-cn/visualstudio/python/debugging-python-in-visual-studio?view=vs-2022)

\[49] vscode在断点旁边写expression让条件为true的时候才触发断点提高调试效率\_vscode 断点表达式-CSDN博客[ https://blog.csdn.net/u013565133/article/details/151903976](https://blog.csdn.net/u013565133/article/details/151903976)

\[50] python vscode条件断点表达式怎么写\_mob649e816880fe的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16175516/12704637](https://blog.51cto.com/u_16175516/12704637)

\[51] VSCode调试技巧进阶\_条件断点与日志点使用-VSCode-PHP中文网[ https://m.php.cn/faq/1757689.html](https://m.php.cn/faq/1757689.html)

\[52] Python程序员Visual Studio Code指南\_visual studio code python-CSDN博客[ https://blog.csdn.net/Saki\_Python/article/details/132469700](https://blog.csdn.net/Saki_Python/article/details/132469700)

\[53] VSCode代码调试进阶:多线程与复杂条件断点-VSCode-PHP中文网[ https://m.php.cn/faq/1722779.html](https://m.php.cn/faq/1722779.html)

\[54] vscode如何对python进行调试 – PingCode[ https://docs.pingcode.com/ask/1163418.html](https://docs.pingcode.com/ask/1163418.html)

\[55] 【AIGC】基础篇:VS Code 配置 Python 命令行参数调试debug超详细教程\_mob6454cc67e023的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16099210/14243129](https://blog.51cto.com/u_16099210/14243129)

\[56] Python debugging in VS Code[ https://code.visualstudio.com/docs/python/debugging/?from\_column=20423\&from=20423](https://code.visualstudio.com/docs/python/debugging/?from_column=20423\&from=20423)

\[57] 调试一个py脚本，怎么设置配置，vscode - CSDN文库[ https://wenku.csdn.net/answer/34harrr76a](https://wenku.csdn.net/answer/34harrr76a)

\[58] Debugging[ https://donjayamanne.github.io/pythonVSCodeDocs/docs/debugging/](https://donjayamanne.github.io/pythonVSCodeDocs/docs/debugging/)

\[59] Python settings reference[ https://vscode-docs-arc.readthedocs.io/en/latest/python/settings-reference/](https://vscode-docs-arc.readthedocs.io/en/latest/python/settings-reference/)

\[60] Mastering Advanced Python Debugging in VSCode in Simple Steps[ https://toxigon.com/advanced-python-debugging-in-vscode](https://toxigon.com/advanced-python-debugging-in-vscode)

\[61] python vscode带参数调试-CSDN博客[ https://blog.csdn.net/qq\_37087723/article/details/140921735](https://blog.csdn.net/qq_37087723/article/details/140921735)

\[62] 在 Visual Studio Code 中调试 Python 应用程序的配置\_Vscode中文网[ https://vscode.github.net.cn/docs/python/debugging](https://vscode.github.net.cn/docs/python/debugging)

\[63] VSCode Python调试配置完整指南-VSCode-PHP中文网[ https://m.php.cn/faq/1714523.html](https://m.php.cn/faq/1714523.html)

\[64] 【分布式训练 debug】VS Code Debug 技巧:launch.json实用参数\_vscode debug launch.json-CSDN博客[ https://blog.csdn.net/weixin\_44212848/article/details/142684478](https://blog.csdn.net/weixin_44212848/article/details/142684478)

\[65] VSCode调试时如何传入命令行参数?\_编程语言-CSDN问答[ https://ask.csdn.net/questions/8757802](https://ask.csdn.net/questions/8757802)

\[66] vscode 运行python时，在输出窗口如何显示，如何在设置(文件)(首选项)(设置)run-code - CSDN文库[ https://wenku.csdn.net/answer/7uip9fzq53](https://wenku.csdn.net/answer/7uip9fzq53)

\[67] 问题:如何在VSCode中配置带参数调试?\_编程语言-CSDN问答[ https://ask.csdn.net/questions/8698472](https://ask.csdn.net/questions/8698472)

\[68] 已安装 Python 扩展(Microsoft 官方)不支持低于3.9的python版本 - CSDN文库[ https://wenku.csdn.net/answer/1pgdkge9ax](https://wenku.csdn.net/answer/1pgdkge9ax)

\[69] Python VSCode Extension[ https://community.chocolatey.org/packages/vscode-python/2025.15.2025091201](https://community.chocolatey.org/packages/vscode-python/2025.15.2025091201)

\[70] Error: Unable to install extension 'ms-python.python' as it is not compatible with VS Code '1.91.1'. - CSDN文库[ https://wenku.csdn.net/answer/1yep2hxoxf](https://wenku.csdn.net/answer/1yep2hxoxf)

\[71] Vscode 识别不到 python 解释器\_mob649e8154f2e5的技术博客\_51CTO博客[ https://blog.51cto.com/u\_16175436/13513873](https://blog.51cto.com/u_16175436/13513873)

\[72] VSCode Jupyter 扩展 v2025.2.0 版本技术解析 - GitCode博客[ https://blog.gitcode.com/d6223856b683e1ba12b7ac872330b91a.html](https://blog.gitcode.com/d6223856b683e1ba12b7ac872330b91a.html)

\[73] 我是说3.7版本的调试配置不用变化吗 - CSDN文库[ https://wenku.csdn.net/answer/4xfj9u5fbo](https://wenku.csdn.net/answer/4xfj9u5fbo)

\[74] 微软:VSCode 决定放弃 Python 3.7\_python 3.7 is no longer supported by the python co-CSDN博客[ https://blog.csdn.net/Z987421/article/details/134149042](https://blog.csdn.net/Z987421/article/details/134149042)

\[75] VsCode更新Python插件以后不支持3.6及之前的语言版本Debug\_python拓展调试器不支持3.6一下-CSDN博客[ https://blog.csdn.net/jst100/article/details/125783925](https://blog.csdn.net/jst100/article/details/125783925)

> （注：文档部分内容可能由 AI 生成）