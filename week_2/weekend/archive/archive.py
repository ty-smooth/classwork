def validate_emails(email, col, index):
    try:
      valid = validate_email(email)
      email = valid.email
    except EmailNotValidError as e:
      logging.error(f"Index: {index}, Column: {col}, Not a valid email address.")




def validate_email(email, col, index):
    is_valid_email = bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

    if not is_valid_email:
        logging.error(f"Index: {index}, Column: {col}, Not a valid email address.")


subset_cols = ["Agent Last Name", "Agent Middle Name", "Agent First Name",
            "Agent Writing Contract Start Date", "Date when an agent became A2O"]
