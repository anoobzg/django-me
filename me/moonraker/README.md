# Moonraker API 模拟器

这是一个模拟 Moonraker API 的 Django 应用。Moonraker 是 Klipper 3D 打印机的 API 服务器。

## API 端点

所有 API 端点都位于 `/api/` 路径下。

### 1. 服务器信息
```
GET /api/server/info
```
返回 Moonraker 服务器信息，包括连接状态、组件列表等。

### 2. 打印机信息
```
GET /api/printer/info
```
返回打印机基本信息，包括状态、版本信息等。

### 3. 查询打印机对象状态
```
GET /api/printer/objects/query?objects=tool0,heater_bed
POST /api/printer/objects/query
```
查询指定打印机对象的状态。

**GET 请求示例：**
```
GET /api/printer/objects/query?objects=tool0,heater_bed,motion_report
```

**POST 请求示例：**
```json
{
  "objects": {
    "tool0": null,
    "heater_bed": null,
    "motion_report": null
  }
}
```

### 4. 列出所有打印机对象
```
GET /api/printer/objects/list
```
返回所有可用的打印机对象列表。

### 5. 打印机完整状态
```
GET /api/printer/status
```
返回打印机的完整状态信息。

## 使用示例

### Python 示例
```python
import requests

# 获取服务器信息
response = requests.get('http://localhost:8000/api/server/info')
print(response.json())

# 获取打印机状态
response = requests.get('http://localhost:8000/api/printer/status')
print(response.json())

# 查询特定对象
response = requests.get('http://localhost:8000/api/printer/objects/query?objects=tool0,heater_bed')
print(response.json())
```

### cURL 示例
```bash
# 获取服务器信息
curl http://localhost:8000/api/server/info

# 获取打印机状态
curl http://localhost:8000/api/printer/status

# 查询对象状态
curl "http://localhost:8000/api/printer/objects/query?objects=tool0,heater_bed"
```

## 响应格式

所有 API 响应都遵循 Moonraker 的标准格式：

```json
{
  "result": {
    // 实际数据
  }
}
```

## 注意事项

- 这是一个模拟器，返回的是模拟数据，不连接真实的打印机
- 所有端点都使用 `@csrf_exempt` 装饰器，方便测试
- 温度和状态值都是模拟的默认值

