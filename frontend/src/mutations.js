import gql from "graphql-tag";

export const UPDATE_CONTACT = gql`
  mutation (
    $contactId: ID!
    $firstName: String!
    $lastName: String!
    $email: String!
    $phone: String!
    $image: Upload!
  ) {
    updateContact(
      contactId: $contactId
      firstName: $firstName
      lastName: $lastName
      email: $email
      phone: $phone
      image: $image
    ) {
      contact {
        id
        firstName
        lastName
        email
        phone
        image
      }
    }
  }
`;

export const CREATE_CONTACT = gql`
  mutation (
    $firstName: String!
    $lastName: String!
    $email: String!
    $phone: String!
    $image: Upload!
  ) {
    createContact(
      firstName: $firstName
      lastName: $lastName
      email: $email
      phone: $phone
      image: $image
    ) {
      contact {
        id
        firstName
        lastName
        email
        phone
        image
      }
    }
  }
`;

export const DELETE_CONTACT = gql`
  mutation ($contactId: ID!) {
    deleteContact(contactId: $contactId) {
      success
    }
  }
`;
