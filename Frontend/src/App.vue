<template>
  <div id="app">
    <header class="app-header">
      <h1>图片公式识别工具</h1>
      <p>支持拖拽、复制粘贴或选择本地图片进行识别</p>
    </header>
    <main class="app-main">
      <UploadAndDrag />
    </main>
    <footer class="app-footer">
      <p>&copy; 2025 图片识别工具 | 支持 OCR 识别</p>
    </footer>
  </div>
</template>

<script>
import UploadAndDrag from "./components/UploadAndDrag.vue";

export default {
  components: {
    UploadAndDrag,
  },
  mounted() {
    document.title = "图片公式识别工具"; // 设置页面标题
  },
};
</script>

