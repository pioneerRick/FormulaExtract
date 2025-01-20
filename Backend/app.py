from flask import Flask, request, jsonify
import os
from OCR_iFLY import get_result

app = Flask(__name__)

# 上传文件的存储路径
UPLOAD_DIR = "./uploaded_images"
CONFIG_PATH = os.getenv("CONFIG_PATH", "./config.ini")  # 配置文件路径
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 检查配置文件是否存在
if not os.path.exists(CONFIG_PATH):
    raise FileNotFoundError(f"配置文件 {CONFIG_PATH} 不存在，请确保文件已创建并包含 API 信息")


# def upload_image():
@app.route('/upload_image/', methods=['POST'])
# @app.route('/api/upload_image/', methods=['POST'])
def upload_image():
    """
    接收单个或多个文件，调用 OCR 识别，返回识别结果
    """
    files = request.files.getlist('file')
    if not files or len(files) == 0:
        return jsonify({"message": "未提供文件"}), 400

    results = []

    for file in files:
        # 检查文件类型
        if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            results.append({
                "file": file.filename,
                "message": "文件类型不支持，仅支持 PNG, JPG, JPEG, BMP 格式"
            })
            continue

        # 保存文件
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        try:
            file.save(file_path)
        except Exception as e:
            results.append({
                "file": file.filename,
                "message": f"文件保存失败: {str(e)}"
            })
            continue

        # 调用 OCR 识别
        try:
            host = "rest-api.xfyun.cn"
            recognizer = get_result(host)
            recognizer.AudioPath = file_path
            latex_result = recognizer.call_url()

            if "错误" in latex_result:
                # 如果识别失败，记录错误信息
                results.append({
                    "file": file.filename,
                    "message": "识别失败",
                    "detail": latex_result
                })
            else:
                # 成功识别，返回结果
                results.append({
                    "file": file.filename,
                    "message": "识别成功",
                    "latex": latex_result
                })
        except Exception as e:
            # 处理异常情况
            results.append({
                "file": file.filename,
                "message": "公式识别失败",
                "detail": str(e)
            })

    # 检查是否有任何有效结果
    if len(results) == 0:
        return jsonify({"message": "没有任何文件被成功处理"}), 400

    return jsonify(results), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=14325,debug=True)
    # app.run(debug=True)





