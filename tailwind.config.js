/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/templates/**/**/**/**/*.html",
    "./src/templates/**/**/**/*.html",
    "./src/templates/**/**/*.html",
    "./src/templates/**/*.html",
    "./src/templates/*.html",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/aspect-ratio"), require("flowbite/plugin")],
};

