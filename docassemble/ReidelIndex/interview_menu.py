def buttons_matching_roles(interview_options, privileges):
  return [ {index: button["label"], "image": button["image"]} for index, button in enumerate(interview_options) if any(set(interview_options[index]['roles']) & set(privileges))]