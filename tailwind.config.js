/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./website/templates/*.html"],
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
};
