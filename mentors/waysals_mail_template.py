####################################################################################

# waysals forget password mail template

####################################################################################

def forget_password_content(name, encrypted_email):
	message = """\
	<html>
	   <body link="#00a5b5" vlink="#00a5b5" alink="#00a5b5" style="margin-top: 20px; margin-bottom: 20px;">
	   <div class="s12">
			<table class=" main contenttable" align="center" style="font-weight: normal;border-collapse: collapse;border: 0;margin-left: auto;margin-right: auto;padding: 0;font-family: Arial, sans-serif;color: #555559;background-color: white;font-size: 16px;line-height: 26px;width: 600px;">
			<tr>
			<td class="border" style="border-collapse: collapse;border: 1px solid #eeeff0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
				<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
					<tr>
						<td colspan="4" valign="top" class="image-section" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;background-color: #fff;border-bottom: 4px solid #00a5b5">
							<a href="https://waysals.com" target="_blank"><img class="top-image" src="https://www.waysals.com/static/images/waysals_logo.png" style="line-height: 1;width: 150px; margin: 10px; margin-top: 15px;" alt="Waysals"></a>
						</td>
					</tr>
					<tr>
						<td valign="top" class="side title" style="border-collapse: collapse;border: 0;margin: 0;padding: 20px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;vertical-align: top;background-color: white;border-top: none;">
							<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
								<tr>
									<td class="head-title" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 28px;line-height: 34px;font-weight: bold; text-align: center;">
										<div class="mktEditable" id="main_title">
											Waysals Password Reset
										</div>
									</td>
								</tr>

								<tr>
									<td class="top-padding" style="border-collapse: collapse;border: 0;margin: 0;padding: 15px 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 21px;">
										<hr size="1" color="#eeeff0">
									</td>
								</tr>
								<tr>
									<td class="text" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
									<div class="mktEditable" id="main_text">
										Hi {name},<br><br>
										We just received your request to reset your password for your Waysals account. Follow the following link to change it:<br><br>
										<div style="text-align: center; font-weight: bold;"><a href="{mail_id}" style="color: #1e88e5;">Click for reset password</a></div><br>
										Didn&apos;t send the request? Feel free to ignore this mail or reply to let us know; we&apos;ll be glad to hear from you!
									</div>
									</td>
								</tr>
								<tr>
									<td style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 24px;">
									 &nbsp;<br>
									</td>
								</tr>
							</table>
						</td>
					</tr>
					<tr>
						<td valign="top" align="center" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
							<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
								<tr>
									<td align="center" valign="middle" class="social" style="border-collapse: collapse;border: 0;margin: 0;padding: 10px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;text-align: center;">
										<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
											<tr>
									<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://twitter.com/waysals/" target="_blank"><img src="https://info.tenable.com/rs/tenable/images/twitter-teal.png"></a></td>
									<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://www.facebook.com/waysals1/" target="_blank"><img src="https://info.tenable.com/rs/tenable/images/facebook-teal.png"></a></td>
									<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://www.linkedin.com/company/14633412/" target="_blank"><img src="https://info.tenable.com/rs/tenable/images/linkedin-teal.png"></a></td>
											</tr>
										</table>
									</td>
								</tr>
							</table>
						</td>
					</tr>
					<tr bgcolor="#fff" style="border-top: 4px solid #00a5b5;">
						<td valign="top" class="footer" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;background: #fff;text-align: center;">
							<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
								<tr>
									<td class="inside-footer" align="center" valign="middle" style="border-collapse: collapse;border: 0;margin: 0;padding: 20px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 12px;line-height: 16px;vertical-align: middle;text-align: center;width: 580px;">
									<div id="address" class="mktEditable">
										<b>Waysals.com</b><br>
										Reynsia Tech Pvt Ltd.<br>
										<a style="color: #00a5b5;" href="https://www.waysals.com/contact/">Contact Us</a>
									</div>
									</td>
								</tr>
							</table>
						</td>
					</tr>
				</table>
			</td>
		</tr>
	</table>
	</div>
  </body>
	</html>
	""".format(name = name, mail_id = encrypted_email)

	return message


####################################################################################

# waysals invitation mail content

####################################################################################

def invitation_mail_content(user_name):
	message = """\

	<html>
	   <body link="#00a5b5" vlink="#00a5b5" alink="#00a5b5" style="margin-top: 20px; margin-bottom: 20px; font-size = 14px;">
	   <div class="s12">
			<table class=" main contenttable" align="center" style="font-weight: normal;border-collapse: collapse;border: 0;margin-left: auto;margin-right: auto;padding: 0;font-family: Arial, sans-serif;color: #555559;background-color: white;font-size: 16px;line-height: 26px;width: 600px;">
			<tr>
			<td class="border" style="border-collapse: collapse;border: 1px solid #eeeff0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
				<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
					<tr>
						<td colspan="4" valign="top" class="image-section" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;background-color: #fff;border-bottom: 4px solid #00a5b5">
							<a href="http://bit.ly/2xyyvov" target="_blank"><img class="top-image" src="https://www.waysals.com/static/images/waysals_logo.png" style="line-height: 1;width: 150px; margin: 10px; margin-top: 15px;" alt="Waysals"></a>
						</td>
					</tr>
					<tr>
						<td valign="top" class="side title" style="border-collapse: collapse;border: 0;margin: 0;padding: 20px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;vertical-align: top;background-color: white;border-top: none;">
							<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
								<tr>
									<td class="head-title" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 28px;line-height: 34px;font-weight: bold; text-align: center;">
										<div class="mktEditable" id="main_title">
											Share your knowledge with your IITK juniors
										</div>
									</td>
								</tr>

								<tr>
									<td class="top-padding" style="border-collapse: collapse;border: 0;margin: 0;padding: 15px 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 21px;">
										<hr size="1" color="#eeeff0">
									</td>
								</tr>
								<tr>
									<td class="text" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
									<div class="mktEditable" id="main_text">
										Hi {name},<br><br>
										Many of the IITK Alumni are coming to Waysals and sharing their experiences which in some way are impacting the lives of IITK students. We know you also have some story to share which can be of struggle, failure, success, etc. of any yours joourney. So why to keep it only to yourself. Please come to waysals and connect with hundreds of IITK students who need direction in their career.<br><br>

										Write your story at: <a href="https://www.waysals.com">Wayslas</a><br><br>
										Best Wishes!<br>
										From Team Waysals

									</div>
									</td>
								</tr>
								<tr>
									<td style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 24px;">
									 &nbsp;<br>
									</td>
								</tr>
							</table>
						</td>
					</tr>
					<tr>
						<td valign="top" align="center" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
							<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
								<tr>
									<td align="center" valign="middle" class="social" style="border-collapse: collapse;border: 0;margin: 0;padding: 10px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;text-align: center;">
										<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
											<tr>
									<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://twitter.com/waysals/" target="_blank"><img src="https://info.tenable.com/rs/tenable/images/twitter-teal.png"></a></td>
									<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://www.facebook.com/waysals1/" target="_blank"><img src="https://info.tenable.com/rs/tenable/images/facebook-teal.png"></a></td>
									<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://www.linkedin.com/company/14633412/" target="_blank"><img src="https://info.tenable.com/rs/tenable/images/linkedin-teal.png"></a></td>
											</tr>
										</table>
									</td>
								</tr>
							</table>
						</td>
					</tr>
					<tr bgcolor="#fff" style="border-top: 4px solid #00a5b5;">
						<td valign="top" class="footer" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;background: #fff;text-align: center;">
							<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
								<tr>
									<td class="inside-footer" align="center" valign="middle" style="border-collapse: collapse;border: 0;margin: 0;padding: 20px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 12px;line-height: 16px;vertical-align: middle;text-align: center;width: 580px;">
									<div id="address" class="mktEditable">
										<b>Waysals.com</b><br>
							 			Reynsia Tech Pvt Ltd.<br>
										<a style="color: #00a5b5;" href="https://www.waysals.com/contact/">Contact Us</a>
									</div>
									</td>
								</tr>
							</table>
						</td>
					</tr>
				</table>
			</td>
		</tr>
	</table>
	</div>
  	</body>
	</html>

	""".format(name = user_name)

	return message



####################################################################################

# waysals general mail to all users

####################################################################################

def general_mail_content(user_name, unsubscribe_link):
	message = """\

	<html>
	   <body link="#00a5b5" vlink="#00a5b5" alink="#00a5b5" style="margin-top: 20px; margin-bottom: 20px; font-size = 14px;">
	   <div class="s12">
			<table class=" main contenttable" align="center" style="font-weight: normal;border-collapse: collapse;border: 0;margin-left: auto;margin-right: auto;padding: 0;font-family: Arial, sans-serif;color: #555559;background-color: white;font-size: 16px;line-height: 26px;width: 600px;">
			<tr>
			<td class="border" style="border-collapse: collapse;border: 1px solid #eeeff0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
				<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
					<tr>
						<td colspan="4" valign="top" class="image-section" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;background-color: #fff;border-bottom: 4px solid #00a5b5">
							<a href="http://bit.ly/2xyyvov" target="_blank"><img class="top-image" src="https://www.waysals.com/static/images/waysals_logo.png" style="line-height: 1;width: 150px; margin: 10px; margin-top: 15px;" alt="Waysals"></a>
						</td>
					</tr>
					<tr>
						<td valign="top" class="side title" style="border-collapse: collapse;border: 0;margin: 0;padding: 20px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;vertical-align: top;background-color: white;border-top: none;">
							<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
								<tr>
									<td class="head-title" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 28px;line-height: 34px;font-weight: bold; text-align: center;">
										<div class="mktEditable" id="main_title">
											Someone is at IITK who needs your help
										</div>
									</td>
								</tr>

								<tr>
									<td class="top-padding" style="border-collapse: collapse;border: 0;margin: 0;padding: 15px 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 21px;">
										<hr size="1" color="#eeeff0">
									</td>
								</tr>
								<tr>
									<td class="text" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
									<div class="mktEditable" id="main_text">
										Hi {name},<br><br>
										This is a dummy mail to test the functionality of mail
										<div style="text-align: center;">To know more please visit: &nbsp;<a href="http://bit.ly/2xyyvov" style="text-decoration = none; font-size: 18px; font-weight: bold;">waysals.com</a></div>
										<br><br>
										Best Wishes!<br>
										From Team Waysals

									</div>
									</td>
								</tr>
								<tr>
									<td style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 24px;">
									 &nbsp;<br>
									</td>
								</tr>
							</table>
						</td>
					</tr>
					<tr>
						<td valign="top" align="center" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
							<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
								<tr>
									<td align="center" valign="middle" class="social" style="border-collapse: collapse;border: 0;margin: 0;padding: 10px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;text-align: center;">
										<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
											<tr>
									<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://twitter.com/waysals/" target="_blank"><img src="https://info.tenable.com/rs/tenable/images/twitter-teal.png"></a></td>
									<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://www.facebook.com/waysals1/" target="_blank"><img src="https://info.tenable.com/rs/tenable/images/facebook-teal.png"></a></td>
									<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://www.linkedin.com/company/14633412/" target="_blank"><img src="https://info.tenable.com/rs/tenable/images/linkedin-teal.png"></a></td>
											</tr>
										</table>
									</td>
								</tr>
							</table>
						</td>
					</tr>
					<tr bgcolor="#fff" style="border-top: 4px solid #00a5b5;">
						<td valign="top" class="footer" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;background: #fff;text-align: center;">
							<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
								<tr>
									<td class="inside-footer" align="center" valign="middle" style="border-collapse: collapse;border: 0;margin: 0;padding: 20px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 12px;line-height: 16px;vertical-align: middle;text-align: center;width: 580px;">
									<div id="address" class="mktEditable">
										<b>Waysals.com</b><br>
							 			Reynsia Tech Pvt Ltd.<br>
										<a style="color: #00a5b5;" href="https://www.waysals.com/contact/">Contact Us</a>
									</div>
									<div id="address" class="mktEditable" style="margin-top: 15px;">
										If you don't want to receive this type of email in the future, please <a style="color: #00a5b5;" href="https://www.waysals.com/contact/"> unsubscribe.</a>
									</div>
									</td>
								</tr>
							</table>
						</td>
					</tr>
				</table>
			</td>
		</tr>
	</table>
	</div>
  	</body>
	</html>

	""".format(name = user_name, unsubscribe_link = unsubscribe_link)

	return message


####################################################################################

# waysals experience mail to all users

####################################################################################

def experience_mail_content(user_name, unsubscribe_link):
	message = """\

	<html>
		<body link="#00a5b5" vlink="#00a5b5" alink="#00a5b5">
		   <div>
				<table class=" main contenttable" align="center" style="font-weight: normal;border-collapse: collapse;border: 0;margin-left: auto;margin-right: auto;padding: 0;font-family: Arial, sans-serif;color: #555559;background-color: white;font-size: 16px;line-height: 26px;width: 600px;">
				<tr>
				<td class="border" style="border-collapse: collapse;border: 1px solid #eeeff0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
					<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
						<tr>
							<td colspan="4" valign="top" class="image-section" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;background-color: #fff;border-bottom: 4px solid #00a5b5">
								<a href="https://waysals.com"><img class="top-image" src="waysals_logo.png" style="line-height: 1;width: 150px; margin: 10px; margin-top: 15px;" alt="Waysals"></a>
							</td>
						</tr>
						<tr>
							<td valign="top" class="side title" style="border-collapse: collapse;border: 0;margin: 0;padding: 20px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;vertical-align: top;background-color: white;border-top: none;">
								<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
								<div id="address" class="mktEditable" style="font-size: 14px; line-height: 0px; margin-top: 20px;">

								  Top Experiences for You

									<tr>
										<td class="top-padding" style="border-collapse: collapse;border: 0;margin: 0;padding: 10px 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 21px;">
											<hr size="1" color="#eeeff0">
										</td>
									</tr>
									<tr>
										<td class="text" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 20px;line-height: 26px;">
										<div class="mktEditable" id="main_text">

										   <b>What do you need to prepare for placements?: My Placement Perspective </b>

										</div>
										 <div class="mktEditable" id="main_text" style="font-size: 15px; margin-top: 5px;">

										   Campus placements at colleges in the life of any student are very defining moments that students look up for. Each year when college placement time comes, every student shift their gear for the challenge before them.Let us talk about what you need to prepare before placements which can increase your <a style="color: #00a5b5;" href="https://www.waysals.com/contact/">see more...</a>

										</div>
										</td>
									</tr>
									<tr>
										<td style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 24px;">
										 &nbsp;<br>
										</td>
									</tr>
									<tr>
										<td class="top-padding" style="border-collapse: collapse;border: 0;margin: 0;padding: 10px 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 21px;">
											<hr size="1" color="#eeeff0">
										</td>
									</tr>
									<tr>
										<td class="text" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 20px;line-height: 26px;">
										<div class="mktEditable" id="main_text">

										   <b>What do you need to prepare for placements?: My Placement Perspective </b>

										</div>
										 <div class="mktEditable" id="main_text" style="font-size: 15px; margin-top: 5px;">

										   Campus placements at colleges in the life of any student are very defining moments that students look up for. Each year when college placement time comes, every student shift their gear for the challenge before them.Let us talk about what you need to prepare before placements which can increase your <a style="color: #00a5b5;" href="https://www.waysals.com/contact/">see more...</a>

										</div>
										 <div class="mktEditable" id="main_text" style="font-size: 15px; margin-top: 25px; text-align: center;">

										   <span href="" style="font-size: 100%; padding: 6px; padding-right: 15px; padding-left: 15px; color:  #fff; border: 0px solid #bdbdbd; border-radius: 2%/10%; text-decoration: none; cursor: pointer; transition: all 0.3s ease-out;background-color: #00a5b5; margin-top: 12px;">Read More...</span>

										</div>
										</td>
									</tr>
									<tr>
										<td style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 24px;">
										 &nbsp;<br>
										</td>
									</tr>


								</table>
							</td>
						</tr>
						<tr>
							<td valign="top" align="center" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
								<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
									<tr>
										<td align="center" valign="middle" class="social" style="border-collapse: collapse;border: 0;margin: 0;padding: 10px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;text-align: center;">
											<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
												<tr>
										<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://twitter.com/waysals/"><img src="https://info.tenable.com/rs/tenable/images/twitter-teal.png"></a></td>
										<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://www.facebook.com/waysals1/"><img src="https://info.tenable.com/rs/tenable/images/facebook-teal.png"></a></td>
										<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://www.linkedin.com/company/14633412/admin/"><img src="https://info.tenable.com/rs/tenable/images/linkedin-teal.png"></a></td>

												</tr>
											</table>
										</td>
									</tr>
								</table>
							</td>
						</tr>
						<tr bgcolor="#fff" style="border-top: 4px solid #00a5b5;">
							<td valign="top" class="footer" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;background: #fff;text-align: center;">
								<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
									<tr>
										<td class="inside-footer" align="center" valign="middle" style="border-collapse: collapse;border: 0;margin: 0;padding: 20px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 12px;line-height: 16px;vertical-align: middle;text-align: center;width: 580px;">
											<div id="address" class="mktEditable">
												<b>Waysals.com</b><br>
									 			Reynsia Tech Pvt Ltd.<br>
												<a style="color: #00a5b5;" href="https://www.waysals.com/contact/">Contact Us</a>
											</div>
											<div id="address" class="mktEditable" style="margin-top: 15px;">
												If you don't want to receive this type of email in the future, please <a style="color: #00a5b5;" href="https://www.waysals.com/contact/"> unsubscribe.</a>
											</div>
										</td>
									</tr>

								</table>
							</td>
						</tr>
					</table>
				</td>
				</tr>
				</table>
			</div>
		</body>
	</html>

	""".format(name = user_name, unsubscribe_link = unsubscribe_link)

	return message



####################################################################################

# waysals question asking mail to all users

####################################################################################

def question_mail_content(user_name, unsubscribe_link):
	message = """\

	<html>
		<body link="#00a5b5" vlink="#00a5b5" alink="#00a5b5">

		   <div class="s12">

				<table class=" main contenttable" align="center" style="font-weight: normal;border-collapse: collapse;border: 0;margin-left: auto;margin-right: auto;padding: 0;font-family: Arial, sans-serif;color: #555559;background-color: white;font-size: 16px;line-height: 26px;width: 600px;">
				<tr>
				<td class="border" style="border-collapse: collapse;border: 1px solid #eeeff0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
					<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
						<tr>
							<td colspan="4" valign="top" class="image-section" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;background-color: #fff;border-bottom: 4px solid #00a5b5">
								<a href="https://waysals.com"><img class="top-image" src="waysals_logo.png" style="line-height: 1;width: 150px; margin: 10px; margin-top: 15px;" alt="Waysals"></a>

							</td>
						</tr>


						<tr>
							<td valign="top" class="side title" style="border-collapse: collapse;border: 0;margin: 0;padding: 20px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;vertical-align: top;background-color: white;border-top: none;">
								<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">

								 <div class="mktEditable" id="main_text" style="line-height: 0px; margin-top: 20px; font-size: 14px;">

										   Can you answer this question?

										</div>

										<tr>
										<td class="top-padding" style="border-collapse: collapse;border: 0;margin: 0;padding: 10px 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 21px;">
											<hr size="1" color="#eeeff0">
										</td>
									</tr>

									<tr>
										<td class="text" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 20px;line-height: 26px;">
										<div class="mktEditable" id="main_text" style="font-size: 14px;">

										   <b>Ashish Ranjan</b>

										</div>
										<div class="mktEditable" id="main_text" style="font-size: 12px; margin-top: 0px; line-height: 10px; margin-bottom: 10px;">

										   IIT Kanpur, cse

										</div>
										<div class="mktEditable" id="main_text">

										   <b>What do you need to prepare for placements?: My Placement Perspective </b>

										</div>
										 <div class="mktEditable" id="main_text" style="font-size: 15px; margin-top: 15px;">

										   <span href="" style="font-size: 100%; padding: 6px; padding-right: 15px; padding-left: 15px; color:  #fff; border: 0px solid #bdbdbd; border-radius: 2%/10%; text-decoration: none; cursor: pointer; transition: all 0.3s ease-out;background-color: #00a5b5; margin-top: 12px;">Write Answer</span>

										</div>
										<div id="address" class="mktEditable" style="margin-top: 15px; font-size: 13px;">
											 Can't answer this question?
											<a style="color: #00a5b5;" href="https://www.waysals.com/contact/">Pass on this question.</a>
										 </div>
										</td>
									</tr>

								</table>
							</td>
						</tr>
						<tr>
							<td valign="top" align="center" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
								<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
									<tr>
										<td align="center" valign="middle" class="social" style="border-collapse: collapse;border: 0;margin: 0;padding: 10px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;text-align: center;">
											<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
												<tr>
										<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://twitter.com/waysals/"><img src="https://info.tenable.com/rs/tenable/images/twitter-teal.png"></a></td>
										<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://www.facebook.com/waysals1/"><img src="https://info.tenable.com/rs/tenable/images/facebook-teal.png"></a></td>
										<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://www.linkedin.com/company/14633412/admin/"><img src="https://info.tenable.com/rs/tenable/images/linkedin-teal.png"></a></td>

												</tr>
											</table>
										</td>
									</tr>
								</table>
							</td>
						</tr>
						<tr bgcolor="#fff" style="border-top: 4px solid #00a5b5;">
							<td valign="top" class="footer" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;background: #fff;text-align: center;">
								<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
									<tr>
										<td class="inside-footer" align="center" valign="middle" style="border-collapse: collapse;border: 0;margin: 0;padding: 20px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 12px;line-height: 16px;vertical-align: middle;text-align: center;width: 580px;">
											<div id="address" class="mktEditable">
												<b>Waysals.com</b><br>
												rensia tech pvt ltd.<br>
												<a style="color: #00a5b5;" href="https://www.waysals.com/contact/">Contact Us</a>
											</div>
											<div id="address" class="mktEditable" style="margin-top: 15px;">
												If you don't want to receive this type of email in the future, please
												<a style="color: #00a5b5;" href="https://www.waysals.com/contact/"> unsubscribe.</a>
											</div>
										</td>
									</tr>

								</table>
							</td>
						</tr>
					</table>
				</td>
				</tr>
				</table>
			</div>
		</body>
	</html>


	""".format(name = user_name, unsubscribe_link = unsubscribe_link)

	return message








####################################################################################

# waysals send experience mail to user

####################################################################################




def send_experience_mail_to_user(exp_title, exp_text, exp_url_link, unsubscribe_link):
	message = """\

	<html>
		<body link="#00a5b5" vlink="#00a5b5" alink="#00a5b5">
		   <div class="s12">
				<table class=" main contenttable" align="center" style="font-weight: normal;border-collapse: collapse;border: 0;margin-left: auto;margin-right: auto;padding: 0;font-family: Arial, sans-serif;color: #555559;background-color: white;font-size: 16px;line-height: 26px;width: 600px;">
				<tr>
				<td class="border" style="border-collapse: collapse;border: 1px solid #eeeff0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
					<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
						<tr>
							<td colspan="4" valign="top" class="image-section" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;background-color: #fff;border-bottom: 4px solid #00a5b5">
								<a href="https://waysals.com"><img class="top-image" src="https://www.waysals.com/static/images/waysals_logo.png" style="line-height: 1;width: 150px; margin: 10px; margin-top: 15px;" alt="Waysals"></a>
							</td>
						</tr>
						<tr>
							<td valign="top" class="side title" style="border-collapse: collapse;border: 0;margin: 0;padding: 20px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;vertical-align: top;background-color: white;border-top: none;">
								<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
								<div id="address" class="mktEditable" style="font-size: 14px; line-height: 20px; margin-top: 10px;">

								  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,

								</div>

									<tr>
										<td class="top-padding" style="border-collapse: collapse;border: 0;margin: 0;padding: 10px 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 21px;">
											<hr size="1" color="#eeeff0">
										</td>
									</tr>

									<tr>
										<td style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 24px;">
										 &nbsp;<br>
										</td>
									</tr>

									<tr>
										<td class="text" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 20px;line-height: 26px;">
										<div class="mktEditable" id="main_text">

										   <b>{exp_title}</b>

										</div>
										 <div class="mktEditable" id="main_text" style="font-size: 15px; margin-top: 5px;">

										   {exp_text} <a style="color: #00a5b5;" href="{exp_url_link}">see more...</a>

										</div>
										</td>
									</tr>
									<tr>
										<td style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 24px;">
										 &nbsp;<br>
										</td>
									</tr>
									<tr>
										<td class="top-padding" style="border-collapse: collapse;border: 0;margin: 0;padding: 10px 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 21px;">
											<hr size="1" color="#eeeff0">
										</td>
									</tr>
									<tr>
										<td class="text" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 20px;line-height: 26px;">

										 <div class="mktEditable" id="main_text" style="font-size: 14px; margin-top: 5px;">

										   Campus placements at colleges in the life of any student

										</div>
										 <div class="mktEditable" id="main_text" style="font-size: 15px; margin-top: 25px; text-align: center;">

										   <span href="" style="font-size: 100%; padding: 6px; padding-right: 15px; padding-left: 15px; color:  #fff; border: 0px solid #bdbdbd; border-radius: 2%/10%; text-decoration: none; cursor: pointer; transition: all 0.3s ease-out;background-color: #00a5b5; margin-top: 12px;">Read More...</span>

										</div>
										</td>
									</tr>
									<tr>
										<td style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 24px;">
										 &nbsp;<br>
										</td>
									</tr>


								</table>
							</td>
						</tr>
						<tr>
							<td valign="top" align="center" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;">
								<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
									<tr>
										<td align="center" valign="middle" class="social" style="border-collapse: collapse;border: 0;margin: 0;padding: 10px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;text-align: center;">
											<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
												<tr>
										<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://twitter.com/waysals/"><img src="https://info.tenable.com/rs/tenable/images/twitter-teal.png"></a></td>
										<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://www.facebook.com/waysals1/"><img src="https://info.tenable.com/rs/tenable/images/facebook-teal.png"></a></td>
										<td style="border-collapse: collapse;border: 0;margin: 0;padding: 5px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;"><a href="https://www.linkedin.com/company/14633412/admin/"><img src="https://info.tenable.com/rs/tenable/images/linkedin-teal.png"></a></td>

												</tr>
											</table>
										</td>
									</tr>
								</table>
							</td>
						</tr>
						<tr bgcolor="#fff" style="border-top: 4px solid #00a5b5;">
							<td valign="top" class="footer" style="border-collapse: collapse;border: 0;margin: 0;padding: 0;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 16px;line-height: 26px;background: #fff;text-align: center;">
								<table style="font-weight: normal;border-collapse: collapse;border: 0;margin: 0;padding: 0;font-family: Arial, sans-serif;">
									<tr>
										<td class="inside-footer" align="center" valign="middle" style="border-collapse: collapse;border: 0;margin: 0;padding: 20px;-webkit-text-size-adjust: none;color: #555559;font-family: Arial, sans-serif;font-size: 12px;line-height: 16px;vertical-align: middle;text-align: center;width: 580px;">
											<div id="address" class="mktEditable">
												<b>Waysals.com</b><br>
												Reynsia Tech Pvt Ltd.<br>
												<a style="color: #00a5b5;" href="https://www.waysals.com/contact/">Contact Us</a>
											</div>
											<div id="address" class="mktEditable" style="margin-top: 15px;">
												If you don't want to receive this type of email in the future, please <a style="color: #00a5b5;" href="{unsubscribe_link}"> unsubscribe.</a>
											</div>
										</td>
									</tr>

								</table>
							</td>
						</tr>
					</table>
				</td>
				</tr>
				</table>
			</div>
		</body>
	</html>

	""".format(exp_title = exp_title, exp_text = exp_text, exp_url_link = exp_url_link, unsubscribe_link = unsubscribe_link)
	# message = message.strip()
	return message
