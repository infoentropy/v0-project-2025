# Page: Starter Single Column

**Mockup:** single-column  
**Status:** Template (fill in variables before sending)

---

## Components Used

| Order | Component | File |
|---|---|---|
| 1 | Header | `02-components/header/` |
| 2 | Hero Banner | `02-components/hero-banner/` |
| 3 | Text Block | `02-components/text-block/` |
| 4 | CTA Button | `02-components/cta-button/` |
| 5 | Footer | `02-components/footer/` |

---

## Variables Required

Fill these before using this template:

| Variable | Description |
|---|---|
| `{{logo_url}}` | Hosted URL of the brand logo image |
| `{{logo_alt}}` | Alt text for the logo |
| `{{hero_image_url}}` | Hosted URL of the hero image |
| `{{hero_alt}}` | Alt text for the hero image |
| `{{headline}}` | Main headline text |
| `{{body_copy}}` | Body paragraph(s) — plain text or simple HTML |
| `{{cta_label}}` | Button label |
| `{{cta_url}}` | Button destination URL |
| `{{unsubscribe_url}}` | Unsubscribe link |
| `{{company_name}}` | Legal entity name for footer |
| `{{company_address}}` | Physical mailing address for footer |

---

## Full HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <title>Email</title>
</head>
<body style="margin: 0; padding: 0; background-color: #f4f4f4;">

  <!-- Page wrapper -->
  <table role="presentation" cellspacing="0" cellpadding="0" border="0"
         width="100%" style="background-color: #f4f4f4;">
    <tr>
      <td align="center" style="padding: 24px 0;">

        <!-- Content column -->
        <table role="presentation" cellspacing="0" cellpadding="0" border="0"
               width="600" style="background-color: #ffffff;">

          <!-- HEADER -->
          <tr>
            <td align="center" style="padding: 24px;">
              <a href="{{cta_url}}" target="_blank">
                <img src="{{logo_url}}" alt="{{logo_alt}}"
                     width="160" style="display: block; border: 0;" />
              </a>
            </td>
          </tr>

          <!-- HERO BANNER -->
          <tr>
            <td>
              <img src="{{hero_image_url}}" alt="{{hero_alt}}"
                   width="600" style="display: block; border: 0;" />
            </td>
          </tr>

          <!-- BODY COPY -->
          <tr>
            <td style="padding: 32px 24px 16px;">
              <h1 style="margin: 0 0 16px; font-family: Arial, sans-serif;
                         font-size: 24px; font-weight: bold; color: #111111;
                         line-height: 1.3;">
                {{headline}}
              </h1>
              <p style="margin: 0; font-family: Arial, sans-serif;
                        font-size: 16px; color: #444444; line-height: 1.6;">
                {{body_copy}}
              </p>
            </td>
          </tr>

          <!-- CTA BUTTON -->
          <tr>
            <td align="center" style="padding: 24px;">
              <table role="presentation" cellspacing="0" cellpadding="0"
                     border="0" align="center" style="margin: 0 auto;">
                <tr>
                  <td align="center" bgcolor="#000000"
                      style="border-radius: 4px;">
                    <a href="{{cta_url}}" target="_blank"
                       style="display: inline-block;
                              font-family: Arial, sans-serif;
                              font-size: 16px; font-weight: bold;
                              color: #ffffff; text-decoration: none;
                              padding: 14px 28px; border-radius: 4px;
                              background-color: #000000;
                              mso-padding-alt: 0;">
                      {{cta_label}}
                    </a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- FOOTER -->
          <tr>
            <td style="padding: 24px; border-top: 1px solid #e4e4e4;">
              <p style="margin: 0; font-family: Arial, sans-serif;
                        font-size: 12px; color: #999999; text-align: center;
                        line-height: 1.6;">
                {{company_name}} · {{company_address}}<br />
                <a href="{{unsubscribe_url}}"
                   style="color: #999999; text-decoration: underline;">
                  Unsubscribe
                </a>
              </p>
            </td>
          </tr>

        </table>
        <!-- /Content column -->

      </td>
    </tr>
  </table>
  <!-- /Page wrapper -->

</body>
</html>
```
