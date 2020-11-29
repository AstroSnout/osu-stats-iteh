<template>
  <div class="faq-content">
      <FAQItem v-for="item in faqItems" :key="item.id" :content="item" />
  </div>
</template>

<script>
import FAQItem from "./FAQItem.vue";

export default {
  name: "FAQSection",
  components: {
    FAQItem
  },
  data() {
    return {
      faqItems: [
        {
          id: 1,
          question: "How it works?",
          answer: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc elementum, nisi sed vulputate tristique, ex ipsum rutrum dolor, eu cursus magna libero vel ipsum. Aliquam laoreet quis nisl ac consequat. Morbi nisl erat, venenatis quis nulla molestie, pellentesque viverra magna. Mauris et elit vehicula massa placerat tincidunt. Suspendisse id sapien nec mauris mattis faucibus. Sed eu odio ut turpis euismod tristique. Donec feugiat porta diam, at consequat nunc semper non. Aliquam ac diam condimentum, consequat neque ut, convallis metus. Curabitur vitae sollicitudin ante, nec sagittis sapien. Sed in neque eu dolor porttitor scelerisque id eu tellus. Donec id arcu diam."
        },
        {
          id: 2,
          question: "Who is this for?",
          answer: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc elementum, nisi sed vulputate tristique, ex ipsum rutrum dolor, eu cursus magna libero vel ipsum. Aliquam laoreet quis nisl ac consequat. Morbi nisl erat, venenatis quis nulla molestie, pellentesque viverra magna. Mauris et elit vehicula massa placerat tincidunt. Suspendisse id sapien nec mauris mattis faucibus. Sed eu odio ut turpis euismod tristique. Donec feugiat porta diam, at consequat nunc semper non. Aliquam ac diam condimentum, consequat neque ut, convallis metus. Curabitur vitae sollicitudin ante, nec sagittis sapien. Sed in neque eu dolor porttitor scelerisque id eu tellus. Donec id arcu diam."
        },
        {
          id: 3,
          question: "Who made this project?",
          answer: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc elementum, nisi sed vulputate tristique, ex ipsum rutrum dolor, eu cursus magna libero vel ipsum. Aliquam laoreet quis nisl ac consequat. Morbi nisl erat, venenatis quis nulla molestie, pellentesque viverra magna. Mauris et elit vehicula massa placerat tincidunt. Suspendisse id sapien nec mauris mattis faucibus. Sed eu odio ut turpis euismod tristique. Donec feugiat porta diam, at consequat nunc semper non. Aliquam ac diam condimentum, consequat neque ut, convallis metus. Curabitur vitae sollicitudin ante, nec sagittis sapien. Sed in neque eu dolor porttitor scelerisque id eu tellus. Donec id arcu diam."
        },
        {
          id: 4,
          question: "How to get in touch?",
          answer: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc elementum, nisi sed vulputate tristique, ex ipsum rutrum dolor, eu cursus magna libero vel ipsum. Aliquam laoreet quis nisl ac consequat. Morbi nisl erat, venenatis quis nulla molestie, pellentesque viverra magna. Mauris et elit vehicula massa placerat tincidunt. Suspendisse id sapien nec mauris mattis faucibus. Sed eu odio ut turpis euismod tristique. Donec feugiat porta diam, at consequat nunc semper non. Aliquam ac diam condimentum, consequat neque ut, convallis metus. Curabitur vitae sollicitudin ante, nec sagittis sapien. Sed in neque eu dolor porttitor scelerisque id eu tellus. Donec id arcu diam."
        }
      ]
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

.faq-content {
  height: 685px;
  margin: 0 auto;
  /* background-color: #299bf3; */
  border-radius: 0 0 20px 20px;
  padding-left: 4px;
}

.scrollable-content {
  height: 690px;
  overflow: auto;
  overflow-x: hidden;
  background-color: #272f35;
}

.scrollable-content::-webkit-scrollbar {
  width: 4px;
  margin: 0;
}
.scrollable-content::-webkit-scrollbar-track {
  background: #cccccc00;
  margin: 0;
}
.scrollable-content::-webkit-scrollbar-thumb {
  background: #5ae4ff;
  border-radius: 2px;
  margin: 0;
}

.content-row-enter-active,
.content-row-leave-active {
  transition: opacity 0.2s;
}
.content-row-enter,
.content-row-leave-to {
  opacity: 0;
}

/* .content-row-leave-active,
.content-row-enter-active {
  transition: 0.2s ease-in-out;
}
.content-row-enter {
  transform: translate(50%, 0);
}
.content-row-leave-to {
  transform: translate(-50%, 0);
} */
</style>
