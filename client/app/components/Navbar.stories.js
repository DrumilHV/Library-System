import Navbar from "./Navbar";
// import { withNextRouter } from "storybook-addon-next-router";

export default {
  title: "Components/Nabar",
  component: Navbar,
  //   decorators: [withNextRouter()],
  tags: ["autodocs"],
  argTypes: {},
};

export const navbar = {
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
