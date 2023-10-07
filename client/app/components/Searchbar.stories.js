import SearchBar from "./Searchbar";
export default {
  title: "Components/Searchbar",
  component: SearchBar,
  tags: ["autodocs"],
  argTypes: {},
};
export const searchbar = {
  parameters: {
    nextjs: {
      appDirectory: true,
      navigation: {
        pathname: "/",
        query: {},
      },
    },
  },
};
