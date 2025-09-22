---
license: cc-by-4.0
---
## FinSearchComp 评测集

ByteSeedXpert/FinSearchComp

https://huggingface.co/datasets/ByteSeedXpert/FinSearchComp

## 数据字段
### 必需字段（每个对象都有）：
- `prompt_id` - 提示ID
- `prompt` - 问题内容
- `response_reference` - 参考答案
- `judge_prompt_template` - 评判提示模板
- `judge_system_prompt` - 评判系统提示
- `label` - 标签

### 可选字段（可能没有）：
- `wind_ticker` - Wind代码
- `akshare_ticker` - AKShare代码
- `ground_truth` - 真实答案
- `time` - 时间
- `response_reference_translate` - 参考答案翻译
- `yfinance_ticker` - Yahoo Finance代码