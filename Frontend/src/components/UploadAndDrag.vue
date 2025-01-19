<template>
  <div>
    <!-- 文件上传区域 -->
    <div class="canvas-wrapper" id="uploadcanvas" @dragover.prevent @drop="handleDrop" @paste="handlePaste">
      <div>
        <input type="file" id="fileInput" @change="handleFileUpload" hidden />
        <button @click="triggerFileInput" class="file_upload_local">选择文件上传</button>
        <span class="copy-instruction">或者直接复制图片到此区域</span>
      </div>
      <div class="image-preview" v-if="fileArr.length > 0">
        <img v-if="isImage(fileArr[0])" :src="fileArr[0].preview" alt="图片预览" class="image-preview-img"/>
        <p v-else>{{ fileArr[0].name }}</p>
      </div>
    </div>

    <!-- 加载状态 -->
    <div v-if="loading" class="loading">上传中，请稍后...</div>

    <!-- 公式解析结果区域 -->
    <div class="result-wrapper">
      <h3>识别结果</h3>
      <div class="result-box" v-if="latexResult">
        <pre>{{ latexResult }}</pre>
      </div>
      <div v-else class="empty-result">当前没有解析结果</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      fileArr: [], // 文件列表，只保存最近的一张图片
      latexResult: "", // 识别结果
      loading: false, // 加载状态
    };
  },
  methods: {
    // 打开文件选择框
    triggerFileInput() {
      document.getElementById("fileInput").click();
    },
    // 处理文件上传
    handleFileUpload(event) {
      const files = event.target.files;
      if (files.length > 0) {
        this.resizeAndUpload(files[0]); // 调用图片缩放并上传
        event.target.value = ""; // 重置文件选择框状态
      }
    },
    // 处理拖拽图片
    handleDrop(event) {
      const files = event.dataTransfer.files;
      if (files.length > 0) {
        this.resizeAndUpload(files[0]); // 调用图片缩放并上传
      }
    },
    // 处理粘贴图片
    handlePaste(event) {
      const items = event.clipboardData.items;
      for (let item of items) {
        if (item.type.startsWith("image/")) {
          const file = item.getAsFile();
          this.resizeAndUpload(file); // 调用图片缩放并上传
          break; // 仅处理第一张图片
        }
      }
    },
    // 校验文件类型
    validateFile(file) {
      if (!file.type.startsWith("image/")) {
        alert(`文件 ${file.name} 不是图片类型，请重新选择！`);
        return false;
      }
      return true;
    },
    // 图片缩放到固定大小并上传
    resizeAndUpload(file) {
      if (!this.validateFile(file)) return;

      const maxWidth = 600; // 设置最大宽度
      const maxHeight = 400; // 设置最大高度

      const reader = new FileReader();
      reader.readAsDataURL(file);

      reader.onload = (e) => {
        const img = new Image();
        img.src = e.target.result;

        img.onload = () => {
          const canvas = document.createElement("canvas");
          const ctx = canvas.getContext("2d");

          // 计算缩放比例
          let width = img.width;
          let height = img.height;
          const aspectRatio = width / height;

          if (width > maxWidth || height > maxHeight) {
            if (width > height) {
              width = maxWidth;
              height = maxWidth / aspectRatio;
            } else {
              height = maxHeight;
              width = maxHeight * aspectRatio;
            }
          }

          // 设置画布大小
          canvas.width = width;
          canvas.height = height;

          // 绘制缩放后的图片
          ctx.drawImage(img, 0, 0, width, height);

          // 将缩放后的图片数据作为 Blob 上传
          canvas.toBlob((blob) => {
            this.fileArr = [
              {
                file: new File([blob], file.name, { type: file.type }),
                name: file.name,
                preview: canvas.toDataURL(file.type),
              },
            ];

            // 自动上传文件
            this.uploadFiles();
          }, file.type);
        };
      };
    },
    // 上传文件并识别
    async uploadFiles() {
      if (this.fileArr.length === 0) {
        alert("请添加文件后上传！");
        return;
      }

      this.loading = true; // 开始加载

      const formData = new FormData();
      formData.append("file", this.fileArr[0].file); // 只上传当前的唯一文件

      try {
        const response = await fetch("/api/upload_image/", {
          method: "POST",
          body: formData,
        });

        const results = await response.json();
        console.log("后端返回结果：", results); // 调试输出

        if (response.ok) {
          // 提取第一个文件的识别结果
          const firstResult = results[0];
          if (firstResult && firstResult.latex) {
            this.latexResult = firstResult.latex;
          } else if (firstResult && firstResult.message) {
            this.latexResult = `错误：${firstResult.message}`;
          } else {
            this.latexResult = "识别失败，请检查图片内容或格式。";
          }
        } else {
          this.latexResult = `上传失败：${results.message || "未知错误"}`;
        }
      } catch (error) {
        console.error("上传失败：", error);
        this.latexResult = "上传失败，请稍后再试！";
      } finally {
        this.loading = false; // 结束加载
      }
    },
    // 判断文件是否是图片
    isImage(file) {
      return file.file.type.startsWith("image/");
    },
  },
};
</script>

