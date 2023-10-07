import Create from "../create/page";

export default {
  title: "Components/CreatePage",
  component: Create,
  //   decorators: [withNextRouter()],
  tags: ["autodocs"],
  argTypes: {
    id: 499,
  },
};

export const createBook = {
  parameters: {
    nextjs: {
      appDirectory: true,
      navigation: {
        pathname: "/",
        query: {},
      },
    },
    id: 499,
  },
};
