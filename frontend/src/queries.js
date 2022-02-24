import gql from "graphql-tag";

export const ALL_CONTACTS = gql`
  query {
    allContacts {
      id
      firstName
      lastName
      image
    }
  }
`;

export const CONTACT_BY_ID = gql`
  query ($id: ID!) {
    contactById(id: $id) {
      id
      firstName
      lastName
      email
      phone
      image
    }
  }
`;
