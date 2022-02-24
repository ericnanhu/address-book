import { ApolloClient, InMemoryCache } from "@apollo/client/core";
import { createApolloProvider } from "@vue/apollo-option";
import { createUploadLink } from "apollo-upload-client";

const httpLink = createUploadLink({
  uri: "http://127.0.0.1:8000/graphql",
});

export const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(),
});

export const apolloProvider = createApolloProvider({
  defaultClient: apolloClient,
});
