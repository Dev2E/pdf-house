module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#003d9b',
        'on-primary': '#ffffff',
        'primary-container': '#0052cc',
        'on-primary-container': '#c4d2ff',
        secondary: '#0059b8',
        'on-secondary': '#ffffff',
        'secondary-container': '#0071e6',
        'on-secondary-container': '#fefcff',
        tertiary: '#3c454d',
        'on-tertiary': '#ffffff',
        'tertiary-container': '#535c65',
        'on-tertiary-container': '#cbd4df',
        error: '#ba1a1a',
        'on-error': '#ffffff',
        'error-container': '#ffdad6',
        'on-error-container': '#93000a',
        surface: '#faf9ff',
        'on-surface': '#051a3e',
        'surface-variant': '#d8e2ff',
        'on-surface-variant': '#434654',
        outline: '#737685',
        'outline-variant': '#c3c6d6',
        'background': '#faf9ff',
        'on-background': '#051a3e',
      },
      fontFamily: {
        'inter': ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
